"""Analyze stage — deep technical analysis for core-track papers (mid tier).

Capped at ``constants.analyze_cap`` papers per run (highest-relevance first) to bound cost.
"""

from __future__ import annotations

import sqlite3

from wam.config import Config
from wam.llm import LLMClient
from wam.logging import get_logger
from wam.pipeline.schemas import PaperAnalysis
from wam.store import papers as ps

log = get_logger("pipeline.analyze")

SYSTEM = ("You are an expert reviewer of World Action Models (embodied/robot foundation "
          "models, VLA, world models). Analyze the paper rigorously and skeptically. Always "
          "write in English, regardless of the paper's language.\n\n"
          "--- PROFILE ---\n{profile}")


def run(cfg: Config, client: LLMClient, conn: sqlite3.Connection,
        limit: int | None = None) -> int:
    cap = limit or int(cfg.get("constants.analyze_cap", 40))
    system = SYSTEM.format(profile=cfg.profile_text())
    todo = ps.needs_analysis(conn, limit=cap)
    log.info("analyzing %d core papers (cap=%d)", len(todo), cap)
    done = 0
    for row in todo:
        user = f"Title: {row['title']}\n\nAbstract: {row['abstract'] or '(none)'}"
        try:
            a = client.complete_json("analyze", system, user, PaperAnalysis,
                                     label="analyze", max_tokens=5000)
        except Exception as e:  # noqa: BLE001
            log.warning("analyze failed for %s: %s", row["id"], e)
            continue
        ps.set_analysis(conn, row["id"], a.model_dump_json())
        done += 1
        if done % 10 == 0:
            conn.commit()
    conn.commit()
    log.info("analyzed %d papers", done)
    return done
