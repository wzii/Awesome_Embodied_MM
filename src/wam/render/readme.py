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


def _leaderboard(conn: sqlite3.Connection, top_per: int = 10) -> str:
    """Per-benchmark leaderboards grouped by canonical family (key embodied benchmarks first)."""
    from wam.store.benchmarks import BENCH_FAMILIES, normalize_benchmark

    rows = conn.execute(
        "SELECT model_name, training_dataset, benchmark, task, metric_name, metric_value, "
        "claimed_by_authors FROM benchmarks WHERE metric_value IS NOT NULL").fetchall()
    if not rows:
        return "_No benchmark results extracted yet._\n"
    fam: dict[str, list] = {}
    for r in rows:
        f = normalize_benchmark(r["benchmark"])
        if f:
            fam.setdefault(f, []).append(r)
    key = [f for f in BENCH_FAMILIES if f in fam]
    other = sorted((f for f in fam if f not in BENCH_FAMILIES), key=lambda f: -len(fam[f]))
    out = ["_Model identity = (model, training data); same name on different data is a distinct "
           "row. `authors` = self-reported, `3rd-party` = quoted. Higher is better for "
           "success-rate-style metrics._\n"]
    for f in key + other[:12]:
        seen, items = set(), []
        for r in sorted(fam[f], key=lambda x: x["metric_value"], reverse=True):
            k = (r["model_name"], r["training_dataset"], r["metric_name"])
            if k in seen:
                continue
            seen.add(k)
            items.append(r)
            if len(items) >= top_per:
                break
        out.append(f"\n#### {f}  ·  _{len(fam[f])} results_\n")
        out.append("| Model (training data) | Task | Metric | Value | Source |")
        out.append("|-----------------------|------|--------|------:|:------:|")
        for r in items:
            td = f" _({r['training_dataset']})_" if r["training_dataset"] else ""
            src = "authors" if r["claimed_by_authors"] else "3rd-party"
            out.append(f"| {r['model_name']}{td} | {r['task'] or '—'} | {r['metric_name'] or '—'} "
                       f"| {r['metric_value']} | {src} |")
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


_MOM_ICON = {"rising": "📈 rising", "cooling": "📉 cooling", "steady": "➡️ steady"}


def _trends(conn: sqlite3.Connection, limit: int = 12) -> str:
    snap = conn.execute("SELECT max(snapshot_date) FROM fronts").fetchone()[0]
    if not snap:
        return "_No trend snapshot yet._\n"
    rows = conn.execute(
        "SELECT name, summary, size, momentum FROM fronts WHERE snapshot_date=? "
        "ORDER BY size DESC LIMIT ?", (snap, limit)).fetchall()
    if not rows:
        return "_No research fronts detected._\n"
    out = ["| Direction | Papers | Momentum | Summary |", "|-----------|-------:|----------|---------|"]
    for r in rows:
        out.append(f"| **{r['name']}** | {r['size']} | {_MOM_ICON.get(r['momentum'], r['momentum'])} "
                   f"| {_clip(r['summary'], 120)} |")
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
    md = f"""# Awesome-Embodied&MM

> Auto-updated (daily) intelligence on **World Action Models** — world models, vision-language-action
> (VLA) models, action-conditioned video/world generation, robot foundation models, and
> embodied/physical AI. Auto-generated; do not edit by hand.

**Last updated:** {today} · **Tracked:** {c['core']} core · {c['adjacent']} adjacent ·
{c['news']} news · **{c['benchmarks']}** benchmark rows across **{c['variants']}** model
variants · **{c['authors']}** authors

> Scoring: two layers — general (novelty/soundness/impact) + WAM-specific. Top-4 WAM metrics
> (inference **speed**, **gen**eralist, **spec**ialist, inference **cost**) are weighted 2×.
> `–` means the paper does not address that metric (we never fabricate a score).

## 📈 Trends & Popular Directions
{_trends(conn)}
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
_Generated by [Awesome-Embodied&MM](https://github.com/wzii/Awesome_Embodied_MM)._
"""
    (cfg.root / "README.md").write_text(md, encoding="utf-8")
    log.info("wrote README.md")
    return md


def render_digest(cfg: Config, conn: sqlite3.Connection, today: str | None = None) -> str:
    """A full, GitHub-renderable dated issue: that day's new core/adjacent papers + news."""
    today = today or date.today().isoformat()
    new_core = conn.execute(
        "SELECT count(*) FROM papers WHERE track='core' AND first_seen=?", (today,)).fetchone()[0]
    new_adj = conn.execute(
        "SELECT count(*) FROM papers WHERE track='adjacent' AND first_seen=?", (today,)).fetchone()[0]
    lines = [f"# Embodied&MM — {today}\n",
             f"**New today:** {new_core} core · {new_adj} adjacent · "
             f"[full leaderboard & rankings →](../../README.md)\n"]

    core = conn.execute(
        "SELECT title, links_json, scores_json, summary_json FROM papers WHERE track='core' "
        "AND first_seen=? AND scores_json IS NOT NULL "
        "ORDER BY json_extract(scores_json,'$.weighted_total') DESC", (today,)).fetchall()
    lines.append("## 🏆 New core papers\n")
    if not core:
        lines.append("_No new core papers today._\n")
    for r in core:
        s = json.loads(r["scores_json"])
        tldr = json.loads(r["summary_json"] or "{}").get("tldr", "")
        lines.append(f"### {r['title']} · **{s.get('weighted_total','?')}**\n{tldr}\n\n"
                     f"_{_top4_badge(s)}_ · {_link_md(_links(r['links_json']))}\n")

    adj = conn.execute(
        "SELECT title, links_json, innovation_json FROM papers WHERE track='adjacent' "
        "AND first_seen=? AND innovation_json IS NOT NULL ORDER BY relevance DESC", (today,)
    ).fetchall()
    if adj:
        lines.append("## 🔬 New adjacent innovations\n")
        for r in adj:
            inv = json.loads(r["innovation_json"])
            lines.append(f"- **{r['title']}** — {_clip(inv.get('key_idea',''), 220)} "
                         f"{_link_md(_links(r['links_json']))}")
        lines.append("")

    news = conn.execute("SELECT title, authors_json, links_json FROM papers WHERE track='news' "
                        "AND first_seen=? ORDER BY published DESC", (today,)).fetchall()
    if news:
        lines.append("## 📰 News\n")
        for r in news:
            outlet = (json.loads(r["authors_json"] or "[]") or ["—"])[0]
            lines.append(f"- [{r['title']}]({_links(r['links_json']).get('abs','')}) — _{outlet}_")
        lines.append("")

    md = "\n".join(lines)
    out = cfg.root / "data" / "digests"
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{today}.md").write_text(md, encoding="utf-8")
    _write_digest_index(cfg, out)
    log.info("wrote digest %s.md", today)
    return md


def _write_digest_index(cfg: Config, out) -> None:
    """An index of past issues (most recent first) so they're browsable on GitHub."""
    dated = sorted((p.stem for p in out.glob("20*.md")), reverse=True)
    specials = sorted(p.stem for p in out.glob("issue-*.md"))  # e.g. inaugural issue-00
    idx = ["# Awesome-Embodied&MM — past issues\n",
           "Daily issues (newest first). Each links that day's new papers & news.\n"]
    idx += [f"- ⭐ [Issue 0 — Inaugural backlog]({s}.md)" for s in specials]
    idx += [f"- [{d}]({d}.md)" for d in dated]
    (out / "README.md").write_text("\n".join(idx) + "\n", encoding="utf-8")


def render_inaugural_issue(cfg: Config, conn: sqlite3.Connection) -> str:
    """Issue 0 — a one-time comprehensive roundup of the initial backlog (frozen snapshot)."""
    c = _counts(conn)
    md = f"""# Awesome-Embodied&MM — Issue 0 (Inaugural)

> The creation edition: a one-time roundup of the initial ~60-day backlog of World Action
> Models, VLA, world-model and video-generation research. Subsequent issues cover only each
> day's new papers — see the [archive index](README.md).

**Corpus:** {c['core']} core · {c['adjacent']} adjacent · {c['news']} news ·
**{c['benchmarks']}** benchmark rows across **{c['variants']}** model variants ·
**{c['authors']}** authors

## 📈 Trends & Popular Directions
{_trends(conn)}
## 🏆 Top World Action Model Papers
{_core_table(conn)}
## 📊 Benchmark Leaderboards
{_leaderboard(conn)}
## 🔬 Innovation Watch — adjacent fields (VLA / world models / video generation)
{_innovation(conn)}
## 👥 Influential Authors & Groups
{_authors(conn)}
## 📰 Embodied / Physical-AI News
{_news(conn)}
---
_Issue 0 · generated by [Awesome-Embodied&MM](https://github.com/wzii/Awesome_Embodied_MM)._
"""
    out = cfg.root / "data" / "digests"
    out.mkdir(parents=True, exist_ok=True)
    (out / "issue-00.md").write_text(md, encoding="utf-8")
    _write_digest_index(cfg, out)
    log.info("wrote Issue 0 (inaugural) -> data/digests/issue-00.md")
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
