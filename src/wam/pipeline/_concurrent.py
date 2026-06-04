"""Shared helper to run a per-paper LLM stage concurrently.

LLM calls (I/O-bound) run in a thread pool; DB writes happen in the main thread AS results
complete (``as_completed``), committing periodically — so a slow/stuck paper never blocks
committing others, and re-running the stage resumes the unprocessed ones.
"""

from __future__ import annotations

import sqlite3
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable


def run_stage(todo: list, worker: Callable, on_result: Callable, conn: sqlite3.Connection,
              workers: int, label: str, log) -> int:
    """``worker(row) -> (paper_id, obj|None)`` (no DB). ``on_result(paper_id, obj)`` writes."""
    done = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(worker, r) for r in todo]
        for fut in as_completed(futs):
            pid, obj = fut.result()
            if obj is not None:
                on_result(pid, obj)
            done += 1
            if done % 20 == 0:
                conn.commit()
                log.info("%s: %d/%d", label, done, len(todo))
    conn.commit()
    return done
