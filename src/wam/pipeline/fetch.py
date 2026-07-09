"""Fetch + dedup stage.

Gathers candidates from all enabled sources, enriches them (Semantic Scholar citations),
dedups against what's already in the DB, persists the new ones, and updates enrichment on
all seen ones. PwC code-link lookups are deferred to the post-filter shortlist (Phase 3) to
keep this stage cheap. Returns the list of *newly inserted* records.
"""

from __future__ import annotations

import sqlite3
from datetime import date, datetime

from wam.config import Config
from wam.logging import get_logger
from wam.models import PaperRecord
from wam.sources import arxiv, news, openreview, semantic_scholar
from wam.store import papers as paper_store

log = get_logger("pipeline.fetch")


def _norm_title(t: str | None) -> str:
    """Loose title key for cross-source dedup (drops case/punctuation/whitespace)."""
    return "".join(ch for ch in (t or "").lower() if ch.isalnum())


def _record_alert(conn: sqlite3.Connection, kind: str, msg: str) -> None:
    """Persist a durable alert row in `runs` so a silent fetch failure is visible in the
    committed DB (and any dashboard/query over it), not just buried in the run log."""
    try:
        conn.execute(
            "INSERT INTO runs (run_date, stage, n_in, n_out, cost_usd, notes, created_at) "
            "VALUES (?,?,?,?,?,?,?)",
            (date.today().isoformat(), f"alert:{kind}", 0, 0, 0.0, msg,
             datetime.now().isoformat(timespec="seconds")),
        )
        conn.commit()
    except Exception as e:  # noqa: BLE001
        log.warning("failed to record alert row: %s", e)


def gather(cfg: Config) -> list[PaperRecord]:
    """Pull candidates from all sources (no enrichment, no DB writes). Deduped by id.

    Each source is isolated: a failure (e.g. arXiv rate-limit) degrades gracefully rather
    than crashing the whole run.
    """
    records: dict[str, PaperRecord] = {}
    for name, src in (("arxiv", arxiv), ("openreview", openreview), ("news", news)):
        try:
            for rec in src.fetch(cfg):
                records.setdefault(rec.id, rec)
        except Exception as e:  # noqa: BLE001
            log.error("source %s failed, continuing: %s", name, e)
    candidates = list(records.values())
    log.info("gathered %d unique candidates across sources", len(candidates))
    return candidates


def run(cfg: Config, conn: sqlite3.Connection) -> list[PaperRecord]:
    candidates = gather(cfg)
    # Health check / alert: the arXiv query is broad enough that a successful fetch always
    # returns hundreds of in-window papers. Zero arXiv candidates while the source is
    # enabled means the fetch was throttled/failed (see arxiv.ArxivFetchError) — the day's
    # papers will be recovered on the next successful run, but flag it loudly so a run of
    # empty days doesn't pass unnoticed.
    if cfg.get("sources.arxiv.enabled", True) and not any(
            r.source == "arxiv" for r in candidates):
        msg = ("arXiv returned 0 candidates — throttled/failed fetch; "
               "papers recover on the next successful run")
        log.error("🚨 ALERT: %s", msg)
        _record_alert(conn, "arxiv_fetch", msg)
    seen = paper_store.existing_ids(conn)
    new = [r for r in candidates if r.id not in seen]
    # Cross-source title dedup: an OpenReview/news copy of a paper already in the DB (or of
    # another just-fetched candidate) shouldn't be ingested twice. Prefer arXiv as canonical.
    existing_titles = {_norm_title(t) for (t,) in conn.execute("SELECT title FROM papers")}
    deduped: list[PaperRecord] = []
    kept_titles: set[str] = set()
    for r in sorted(new, key=lambda x: 0 if x.source == "arxiv" else 1):
        nt = _norm_title(r.title)
        if nt and (nt in existing_titles or nt in kept_titles):
            continue
        kept_titles.add(nt)
        deduped.append(r)
    if len(deduped) < len(new):
        log.info("title-dedup dropped %d duplicate candidate(s)", len(new) - len(deduped))
    new = deduped
    # Enrich (Semantic Scholar) only the NEW papers — existing ones keep their stored
    # citations, so daily runs don't re-query S2 for the whole corpus.
    try:
        semantic_scholar.enrich(cfg, [r for r in new if r.source != "news"])
    except Exception as e:  # noqa: BLE001
        log.warning("s2 enrichment failed, continuing: %s", e)
    for rec in new:
        paper_store.insert_new(conn, rec)
    conn.commit()
    log.info("persisted: %d new, %d already known", len(new), len(candidates) - len(new))
    return new
