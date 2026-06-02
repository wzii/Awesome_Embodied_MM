"""Summarize stage — structured TL;DR for core + adjacent papers (cheap tier)."""

from __future__ import annotations

import sqlite3

from wam.config import Config
from wam.llm import LLMClient
from wam.logging import get_logger
from wam.pipeline.schemas import PaperSummary
from wam.store import papers as ps

log = get_logger("pipeline.summarize")

SYSTEM = ("Summarize the paper for a World Action Models research digest. Be faithful to the "
          "abstract; do not invent results.")


def run(cfg: Config, client: LLMClient, conn: sqlite3.Connection,
        limit: int | None = None) -> int:
    todo = ps.needs_summary(conn, limit=limit)
    log.info("summarizing %d papers", len(todo))
    done = 0
    for row in todo:
        user = f"Title: {row['title']}\n\nAbstract: {row['abstract'] or '(none)'}"
        try:
            s = client.complete_json("summarize", SYSTEM, user, PaperSummary,
                                     label="summarize", max_tokens=2000)
        except Exception as e:  # noqa: BLE001
            log.warning("summarize failed for %s: %s", row["id"], e)
            continue
        ps.set_summary(conn, row["id"], s.model_dump_json())
        done += 1
        if done % 20 == 0:
            conn.commit()
    conn.commit()
    log.info("summarized %d papers", done)
    return done
