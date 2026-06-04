"""Innovation stage — for adjacent-track papers (VLA / world model / video gen).

No rubric scoring: just the key technical idea and why it could transfer to WAM (mid tier).
"""

from __future__ import annotations

import sqlite3

from wam.config import Config
from wam.llm import LLMClient
from wam.logging import get_logger
from wam.pipeline.schemas import InnovationNote
from wam.store import papers as ps

log = get_logger("pipeline.innovation")

SYSTEM = ("This paper is adjacent to World Action Models (it is VLA / a world model / video "
          "generation, not a WAM itself). Identify its core technical innovation and explain "
          "concretely why/how it could transfer to World Action Models. Always write in "
          "English, regardless of the paper's language.")


def run(cfg: Config, client: LLMClient, conn: sqlite3.Connection,
        limit: int | None = None) -> int:
    from wam.pipeline._concurrent import run_stage
    todo = ps.needs_innovation(conn, limit=limit)
    workers = int(cfg.get("constants.llm_workers", 6))
    log.info("extracting innovation notes for %d adjacent papers (%d workers)", len(todo), workers)

    def worker(row):
        user = f"Title: {row['title']}\n\nAbstract: {row['abstract'] or '(none)'}"
        try:
            return row["id"], client.complete_json("innovation", SYSTEM, user, InnovationNote,
                                                   label="innovation", max_tokens=2000)
        except Exception as e:  # noqa: BLE001
            log.warning("innovation failed for %s: %s", row["id"], e)
            return row["id"], None

    n = run_stage(todo, worker, lambda pid, x: ps.set_innovation(conn, pid, x.model_dump_json()),
                  conn, workers, "innovation", log)
    log.info("innovation notes for %d papers", n)
    return n
