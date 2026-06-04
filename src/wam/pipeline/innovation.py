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
    todo = ps.needs_innovation(conn, limit=limit)
    log.info("extracting innovation notes for %d adjacent papers", len(todo))
    done = 0
    for row in todo:
        user = f"Title: {row['title']}\n\nAbstract: {row['abstract'] or '(none)'}"
        try:
            note = client.complete_json("innovation", SYSTEM, user, InnovationNote,
                                        label="innovation", max_tokens=2000)
        except Exception as e:  # noqa: BLE001
            log.warning("innovation failed for %s: %s", row["id"], e)
            continue
        ps.set_innovation(conn, row["id"], note.model_dump_json())
        done += 1
        if done % 20 == 0:
            conn.commit()
    conn.commit()
    log.info("innovation notes for %d papers", done)
    return done
