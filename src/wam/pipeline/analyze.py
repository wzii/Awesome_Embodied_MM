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
    from wam.pipeline._concurrent import run_stage
    cap = limit or int(cfg.get("constants.analyze_cap", 40))
    system = SYSTEM.format(profile=cfg.profile_text())
    todo = ps.needs_analysis(conn, limit=cap)
    workers = int(cfg.get("constants.llm_workers", 6))
    log.info("analyzing %d core papers (%d workers)", len(todo), workers)

    def worker(row):
        user = f"Title: {row['title']}\n\nAbstract: {row['abstract'] or '(none)'}"
        try:
            return row["id"], client.complete_json("analyze", system, user, PaperAnalysis,
                                                    label="analyze", max_tokens=5000)
        except Exception as e:  # noqa: BLE001
            log.warning("analyze failed for %s: %s", row["id"], e)
            return row["id"], None

    n = run_stage(todo, worker, lambda pid, a: ps.set_analysis(conn, pid, a.model_dump_json()),
                  conn, workers, "analyze", log)
    log.info("analyzed %d papers", n)
    return n
