"""Relevance filter — the cheap-model gate.

Classifies each unfiltered paper into core / adjacent / drop and assigns a 0..1 relevance,
reading the research-interest profile so the call is personalized. News items bypass the LLM
(tagged ``news``). A failed call stores relevance=-1 so it retries next run. The DB `track`
column is the cache: filtered papers are never re-classified.
"""

from __future__ import annotations

import sqlite3

from wam.config import Config
from wam.llm import LLMClient
from wam.logging import COST, get_logger
from wam.pipeline.schemas import RelevanceVerdict
from wam.store import papers as ps

log = get_logger("pipeline.filter")

SYSTEM = ("You triage papers for a World Action Models (WAM) intelligence digest. Use the "
          "profile below to decide the track. Be decisive but inclusive of adjacent work with "
          "transferable techniques. Write the reason in English.\n\n--- PROFILE ---\n{profile}")


def run(cfg: Config, client: LLMClient, conn: sqlite3.Connection,
        limit: int | None = None) -> dict[str, int]:
    profile = cfg.profile_text()
    system = SYSTEM.format(profile=profile)
    threshold = float(cfg.get("constants.relevance_threshold", 0.5))
    counts = {"core": 0, "adjacent": 0, "drop": 0, "news": 0, "error": 0}

    todo = ps.needs_filter(conn, limit=limit)
    log.info("filtering %d papers (threshold=%.2f)", len(todo), threshold)
    for i, row in enumerate(todo):
        if i and i % 25 == 0:
            conn.commit()  # checkpoint so a long run doesn't lose progress on crash
            log.info("filter progress: %d/%d", i, len(todo))
        if row["source"] == "news":
            ps.set_filter(conn, row["id"], "news", 1.0, "news item")
            counts["news"] += 1
            continue
        user = f"Title: {row['title']}\n\nAbstract: {row['abstract'] or '(none)'}"
        try:
            v = client.complete_json("cheap", system, user, RelevanceVerdict,
                                     label="filter", max_tokens=1500)
        except Exception as e:  # noqa: BLE001
            log.warning("filter failed for %s: %s", row["id"], e)
            ps._touch(conn, row["id"], relevance=-1)
            counts["error"] += 1
            continue
        track = "drop" if (v.track == "drop" or v.relevance < threshold) else v.track
        ps.set_filter(conn, row["id"], track, v.relevance, v.reason)
        counts[track] += 1
    conn.commit()
    log.info("filter result: %s", counts)
    return counts
