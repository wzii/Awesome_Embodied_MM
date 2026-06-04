"""Long-context Q&A over the WAM knowledge base (no RAG / no embeddings).

At our scale (~hundreds of tracked papers) the whole corpus's *summaries* + scores +
benchmark leaderboard + author directions + trends fit in a long-context model's window, so
we build a compact "knowledge pack" from SQLite and let the model answer directly with
citations — no retrieval step to miss documents, no vector index to maintain.
"""

from __future__ import annotations

import json
import sqlite3

from wam.config import Config, load_config
from wam.llm import LLMClient
from wam.logging import get_logger
from wam.store import Database

log = get_logger("webapp.qa")

SYSTEM = (
    "You answer questions about World Action Models research. You have two sources:\n"
    "1) the KNOWLEDGE PACK below — our curated corpus (tracked papers with scores, a "
    "benchmark leaderboard, author directions, trends). Use it for facts about what we track.\n"
    "2) WEB SEARCH results (when provided) — use them for the original paper text, definitions "
    "of related concepts, and anything not in the pack.\n"
    "Cite tracked papers by id like (arxiv:2606.01234) and web sources by their URL. Prefer the "
    "pack for our corpus facts; never invent papers, numbers, or citations. Be concise and "
    "concrete, and write in English.")


def build_pack(conn: sqlite3.Connection, max_papers: int = 400,
               include_dropped: bool = True) -> str:
    """Compact, citeable corpus snapshot for the long-context Q&A model."""
    sections: list[str] = []

    papers = conn.execute(
        "SELECT id, title, track, published, scores_json, summary_json FROM papers "
        "WHERE track IN ('core','adjacent') ORDER BY "
        "COALESCE(json_extract(scores_json,'$.weighted_total'),0) DESC LIMIT ?", (max_papers,)
    ).fetchall()
    lines = ["## PAPERS"]
    for r in papers:
        s = json.loads(r["scores_json"]) if r["scores_json"] else {}
        tldr = json.loads(r["summary_json"] or "{}").get("tldr", "") if r["summary_json"] else ""
        score = f" score={s['weighted_total']}" if s.get("weighted_total") is not None else ""
        wam = json.dumps(s.get("wam", {})) if s else ""
        lines.append(f"- ({r['id']}) [{r['track']}{score}] {r['title']} — {tldr}"
                     + (f" wam_scores={wam}" if wam else ""))
    sections.append("\n".join(lines))

    # Dropped papers stay in the KB (title-only) so it still covers them, per project policy.
    if include_dropped:
        drops = conn.execute("SELECT id, title FROM papers WHERE track='drop' "
                             "ORDER BY first_seen DESC LIMIT 200").fetchall()
        if drops:
            sections.append("## OTHER (filtered-out) PAPERS — title only\n"
                            + "\n".join(f"- ({d['id']}) {d['title']}" for d in drops))

    bench = conn.execute(
        "SELECT model_name, training_dataset, benchmark, task, metric_name, metric_value, "
        "claimed_by_authors, source_paper_id FROM benchmarks WHERE metric_value IS NOT NULL "
        "ORDER BY benchmark LIMIT 400").fetchall()
    if bench:
        bl = ["## BENCHMARK LEADERBOARD (model | training data | benchmark | task | metric=value | source)"]
        for b in bench:
            src = "authors" if b["claimed_by_authors"] else "3rd-party"
            bl.append(f"- {b['model_name']} | {b['training_dataset'] or '?'} | {b['benchmark']} | "
                      f"{b['task'] or '-'} | {b['metric_name']}={b['metric_value']} | {src} "
                      f"({b['source_paper_id']})")
        sections.append("\n".join(bl))

    authors = conn.execute(
        "SELECT name, affiliation, directions FROM authors ORDER BY "
        "json_array_length(paper_ids_json) DESC LIMIT 60").fetchall()
    if authors:
        al = ["## INFLUENTIAL AUTHORS"]
        for a in authors:
            al.append(f"- {a['name']}{' ('+a['affiliation']+')' if a['affiliation'] else ''}: "
                      f"{a['directions'] or ''}")
        sections.append("\n".join(al))

    snap = conn.execute("SELECT max(snapshot_date) FROM fronts").fetchone()[0]
    if snap:
        fronts = conn.execute("SELECT name, size, momentum, summary FROM fronts WHERE "
                              "snapshot_date=? ORDER BY size DESC", (snap,)).fetchall()
        fl = ["## TRENDS / DIRECTIONS (name | papers | momentum | summary)"]
        for f in fronts:
            fl.append(f"- {f['name']} | {f['size']} | {f['momentum']} | {f['summary']}")
        sections.append("\n".join(fl))

    return "\n\n".join(sections)


def answer(question: str, history: list[dict] | None = None, cfg: Config | None = None,
           client: LLMClient | None = None) -> dict:
    """Answer a question, optionally with prior conversation turns for multi-turn chat.

    ``history`` is a list of {"role": "user"|"assistant", "content": ...} from earlier turns.
    """
    cfg = cfg or load_config()
    client = client or LLMClient(cfg)
    with Database(cfg) as db:
        pack = build_pack(db.conn, max_papers=int(cfg.get("qa.max_papers", 400)),
                          include_dropped=bool(cfg.get("qa.include_dropped", True)))
    if not pack.strip():
        return {"answer": "The knowledge base is empty — run the pipeline first.", "pack_chars": 0}
    # Optionally let the model also search the web (paper original text, related concepts)
    # via OpenRouter's web plugin — works with any model.
    extra_body = None
    if bool(cfg.get("qa.web_search", True)):
        extra_body = {"plugins": [{"id": "web",
                                   "max_results": int(cfg.get("qa.web_max_results", 5))}]}
    messages = [{"role": "system", "content": f"{SYSTEM}\n\nKNOWLEDGE PACK:\n{pack}"}]
    messages += list(history or [])
    messages.append({"role": "user", "content": question})
    # Generous ceiling: the qa-tier model may be a reasoning model (burns tokens first).
    ans = client.chat("qa", messages, label="qa", max_tokens=6000, extra_body=extra_body)
    return {"answer": ans, "pack_chars": len(pack), "web": bool(extra_body)}
