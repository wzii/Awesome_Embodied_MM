"""Generate the README (awesome list), a daily digest, and a benchmarks CSV export.

All outputs are derived from the SQLite store. Dropped papers stay in the DB/KB but are
excluded from these human-facing surfaces. A link-integrity check flags records missing the
required abstract link.
"""

from __future__ import annotations

import csv
import json
import sqlite3
from datetime import date

from wam.config import Config
from wam.logging import get_logger

log = get_logger("render")

WAM_TOP4 = ["inference_speed", "generalist", "specialist", "inference_cost"]
TOP4_LABEL = {"inference_speed": "spd", "generalist": "gen", "specialist": "spec",
              "inference_cost": "cost"}


def _clip(text: str, n: int) -> str:
    """Truncate at a word boundary with an ellipsis, never mid-word."""
    text = (text or "").strip()
    if len(text) <= n:
        return text
    cut = text[:n].rsplit(" ", 1)[0]
    return cut.rstrip(".,;: ") + "…"


def _links(links_json: str | None) -> dict:
    try:
        return json.loads(links_json or "{}")
    except Exception:  # noqa: BLE001
        return {}


def _link_md(links: dict) -> str:
    parts = []
    for key, label in (("abs", "abs"), ("pdf", "pdf"), ("project_page", "site"),
                       ("code", "code"), ("doi", "doi")):
        if links.get(key):
            parts.append(f"[{label}]({links[key]})")
    return " · ".join(parts) or "—"


def _top4_badge(scores: dict) -> str:
    wam = (scores or {}).get("wam", {})
    cells = []
    for m in WAM_TOP4:
        v = wam.get(m)
        cells.append(f"{TOP4_LABEL[m]} {v if isinstance(v, int) else '–'}")
    return " · ".join(cells)


def _fmt_authors(authors_json: str | None, n: int = 3) -> str:
    a = json.loads(authors_json or "[]")
    return ", ".join(a[:n]) + (" et al." if len(a) > n else "")


# --- sections ---------------------------------------------------------------
def _core_table(conn: sqlite3.Connection, limit: int = 50) -> str:
    rows = conn.execute(
        "SELECT id, title, published, links_json, scores_json FROM papers "
        "WHERE track='core' AND scores_json IS NOT NULL "
        "ORDER BY json_extract(scores_json,'$.weighted_total') DESC LIMIT ?", (limit,)
    ).fetchall()
    if not rows:
        return "_No scored papers yet._\n"
    out = ["| Score | Paper | Published | Top-4 (spd·gen·spec·cost) | Links |",
           "|------:|-------|-----------|---------------------------|-------|"]
    for r in rows:
        s = json.loads(r["scores_json"])
        out.append(f"| **{s.get('weighted_total','?')}** | {r['title']} | "
                   f"{r['published'] or '—'} | {_top4_badge(s)} | {_link_md(_links(r['links_json']))} |")
    return "\n".join(out) + "\n"


def _leaderboard(conn: sqlite3.Connection, limit: int = 40) -> str:
    rows = conn.execute(
        "SELECT model_name, training_dataset, benchmark, task, metric_name, metric_value, "
        "claimed_by_authors FROM benchmarks WHERE metric_value IS NOT NULL "
        "ORDER BY benchmark, metric_value DESC LIMIT ?", (limit,)).fetchall()
    if not rows:
        return "_No benchmark results extracted yet._\n"
    out = ["| Benchmark | Task | Model (training data) | Metric | Value | Source |",
           "|-----------|------|-----------------------|--------|------:|:------:|"]
    for r in rows:
        td = f" _({r['training_dataset']})_" if r["training_dataset"] else ""
        src = "authors" if r["claimed_by_authors"] else "3rd-party"
        out.append(f"| {r['benchmark']} | {r['task'] or '—'} | {r['model_name']}{td} | "
                   f"{r['metric_name'] or '—'} | {r['metric_value']} | {src} |")
    return "\n".join(out) + "\n"


def _innovation(conn: sqlite3.Connection, limit: int = 30) -> str:
    rows = conn.execute(
        "SELECT title, links_json, innovation_json FROM papers WHERE track='adjacent' "
        "AND innovation_json IS NOT NULL ORDER BY relevance DESC LIMIT ?", (limit,)).fetchall()
    if not rows:
        return "_No adjacent-track innovations captured yet._\n"
    out = []
    for r in rows:
        inv = json.loads(r["innovation_json"])
        out.append(f"- **{r['title']}** — {_clip(inv.get('key_idea',''), 320)} "
                   f"_(→ WAM: {_clip(inv.get('transferable_to_wam',''), 260)})_ "
                   f"{_link_md(_links(r['links_json']))}")
    return "\n".join(out) + "\n"


def _authors(conn: sqlite3.Connection, limit: int = 25) -> str:
    rows = conn.execute(
        "SELECT name, affiliation, citations, paper_ids_json, directions, s2_url FROM authors "
        "ORDER BY json_array_length(paper_ids_json) DESC LIMIT ?", (limit,)).fetchall()
    if not rows:
        return "_No authors aggregated yet._\n"
    out = []
    for r in rows:
        n = len(json.loads(r["paper_ids_json"] or "[]"))
        name = f"[{r['name']}]({r['s2_url']})" if r["s2_url"] else r["name"]
        aff = f" · {r['affiliation']}" if r["affiliation"] else ""
        out.append(f"- **{name}** ({n} papers{aff}) — {_clip(r['directions'], 260)}")
    return "\n".join(out) + "\n"


def _news(conn: sqlite3.Connection, limit: int = 15) -> str:
    rows = conn.execute(
        "SELECT title, authors_json, links_json FROM papers WHERE track='news' "
        "ORDER BY published DESC LIMIT ?", (limit,)).fetchall()
    if not rows:
        return "_No news items yet._\n"
    out = []
    for r in rows:
        outlet = (json.loads(r["authors_json"] or "[]") or ["—"])[0]
        link = _links(r["links_json"]).get("abs", "")
        out.append(f"- [{r['title']}]({link}) — _{outlet}_")
    return "\n".join(out) + "\n"


def _counts(conn: sqlite3.Connection) -> dict:
    d = dict(conn.execute("SELECT track, count(*) FROM papers GROUP BY track").fetchall())
    return {"core": d.get("core", 0), "adjacent": d.get("adjacent", 0),
            "drop": d.get("drop", 0), "news": d.get("news", 0),
            "benchmarks": conn.execute("SELECT count(*) FROM benchmarks").fetchone()[0],
            "variants": conn.execute("SELECT count(*) FROM model_variants").fetchone()[0],
            "authors": conn.execute("SELECT count(*) FROM authors").fetchone()[0]}


# --- public -----------------------------------------------------------------
def link_integrity(conn: sqlite3.Connection) -> list[str]:
    issues = []
    for r in conn.execute("SELECT id, links_json FROM papers WHERE track IN ('core','adjacent')"):
        if not _links(r["links_json"]).get("abs"):
            issues.append(f"{r['id']}: missing abstract link")
    return issues


def render_readme(cfg: Config, conn: sqlite3.Connection, today: str | None = None) -> str:
    today = today or date.today().isoformat()
    c = _counts(conn)
    md = f"""# Awesome-WAM

> Daily-updated intelligence on **World Action Models** — world models, vision-language-action
> (VLA) models, action-conditioned video/world generation, robot foundation models, and
> embodied/physical AI. Auto-generated; do not edit by hand.

**Last updated:** {today} · **Tracked:** {c['core']} core · {c['adjacent']} adjacent ·
{c['news']} news · **{c['benchmarks']}** benchmark rows across **{c['variants']}** model
variants · **{c['authors']}** authors

> Scoring: two layers — general (novelty/soundness/impact) + WAM-specific. Top-4 WAM metrics
> (inference **speed**, **gen**eralist, **spec**ialist, inference **cost**) are weighted 2×.
> `–` means the paper does not address that metric (we never fabricate a score).

## 🏆 Top World Action Model Papers
{_core_table(conn)}
## 📊 Benchmark Leaderboard
_Model identity = (name, training dataset); the same name on different data is a distinct row.
Numbers are as reported; `authors` = self-reported, `3rd-party` = quoted comparison._
{_leaderboard(conn)}
## 🔬 Innovation Watch — adjacent fields (VLA / world models / video generation)
_Not scored; surfaced for techniques transferable to WAM._
{_innovation(conn)}
## 👥 Influential Authors & Groups
{_authors(conn)}
## 📰 Embodied / Physical-AI News
{_news(conn)}
---
_Generated by [Awesome-WAM](https://github.com/your-org/Awesome-WAM)._
"""
    (cfg.root / "README.md").write_text(md, encoding="utf-8")
    log.info("wrote README.md")
    return md


def render_digest(cfg: Config, conn: sqlite3.Connection, today: str | None = None) -> str:
    today = today or date.today().isoformat()
    new_core = conn.execute(
        "SELECT count(*) FROM papers WHERE track='core' AND first_seen=?", (today,)).fetchone()[0]
    new_adj = conn.execute(
        "SELECT count(*) FROM papers WHERE track='adjacent' AND first_seen=?", (today,)).fetchone()[0]
    rows = conn.execute(
        "SELECT title, links_json, scores_json, summary_json FROM papers WHERE track='core' "
        "AND first_seen=? AND scores_json IS NOT NULL "
        "ORDER BY json_extract(scores_json,'$.weighted_total') DESC LIMIT 15", (today,)).fetchall()
    lines = [f"# WAM Daily Digest — {today}\n",
             f"**New today:** {new_core} core · {new_adj} adjacent papers\n",
             "## Top new papers\n"]
    if not rows:
        lines.append("_No new scored core papers today._\n")
    for r in rows:
        s = json.loads(r["scores_json"])
        tldr = json.loads(r["summary_json"] or "{}").get("tldr", "")
        lines.append(f"### {r['title']}  ·  **{s.get('weighted_total','?')}**\n"
                     f"{tldr}\n\n_{_top4_badge(s)}_ · {_link_md(_links(r['links_json']))}\n")
    md = "\n".join(lines)
    out = cfg.root / "data" / "digests"
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{today}.md").write_text(md, encoding="utf-8")
    log.info("wrote digest %s.md", today)
    return md


def export_benchmarks_csv(cfg: Config, conn: sqlite3.Connection) -> None:
    cols = ["variant_key", "model_name", "training_dataset", "benchmark", "task", "split",
            "metric_name", "metric_value", "inference_speed", "speed_unit", "inference_cost",
            "cost_unit", "hardware", "source_paper_id", "claimed_by_authors", "notes",
            "extracted_on"]
    rows = conn.execute(f"SELECT {','.join(cols)} FROM benchmarks ORDER BY benchmark, variant_key")
    path = cfg.root / "data" / "benchmarks.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)
    log.info("exported %s", path)
