"""Fetch + dedup stage.

Gathers candidates from all enabled sources, enriches them (Semantic Scholar citations),
dedups against what's already in the DB, persists the new ones, and updates enrichment on
all seen ones. PwC code-link lookups are deferred to the post-filter shortlist (Phase 3) to
keep this stage cheap. Returns the list of *newly inserted* records.
"""

from __future__ import annotations

import sqlite3

from wam.config import Config
from wam.logging import get_logger
from wam.models import PaperRecord
from wam.sources import arxiv, news, semantic_scholar
from wam.store import papers as paper_store

log = get_logger("pipeline.fetch")


def gather(cfg: Config) -> list[PaperRecord]:
    """Pull + enrich candidates from all sources (no DB writes). Deduped by id."""
    records: dict[str, PaperRecord] = {}
    for rec in arxiv.fetch(cfg):
        records.setdefault(rec.id, rec)
    for rec in news.fetch(cfg):
        records.setdefault(rec.id, rec)
    candidates = list(records.values())
    log.info("gathered %d unique candidates across sources", len(candidates))
    semantic_scholar.enrich(cfg, [r for r in candidates if r.source != "news"])
    return candidates


def persist(conn: sqlite3.Connection, candidates: list[PaperRecord]) -> list[PaperRecord]:
    """Insert new records, refresh enrichment on existing. Returns the new ones."""
    seen = paper_store.existing_ids(conn)
    new = [r for r in candidates if r.id not in seen]
    for rec in candidates:
        if rec.id in seen:
            paper_store.update_enrichment(conn, rec)
        else:
            paper_store.insert_new(conn, rec)
    conn.commit()
    log.info("persisted: %d new, %d already known", len(new), len(candidates) - len(new))
    return new


def run(cfg: Config, conn: sqlite3.Connection) -> list[PaperRecord]:
    candidates = gather(cfg)
    return persist(conn, candidates)
