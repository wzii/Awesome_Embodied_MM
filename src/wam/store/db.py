"""SQLite access layer.

The DB is the canonical store; everything else (README, web app, digests) is exported from
it. This module just handles connection + schema init + a couple of low-level helpers; the
domain-specific upserts (papers, benchmarks, people, fronts) live in their own store modules
added in later phases.
"""

from __future__ import annotations

import sqlite3
from datetime import date, datetime
from pathlib import Path

from wam.config import Config, load_config
from wam.logging import get_logger

log = get_logger("store")

SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def connect(db_path: str | Path) -> sqlite3.Connection:
    """Open a connection with row access by name and schema applied."""
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    return conn


class Database:
    """Convenience wrapper around a connection bound to the configured DB path."""

    def __init__(self, config: Config | None = None, db_path: str | Path | None = None):
        self.cfg = config or load_config()
        self.path = Path(db_path) if db_path else self.cfg.path("db")
        self.conn = connect(self.path)
        log.debug("opened db at %s", self.path)

    def __enter__(self) -> "Database":
        return self

    def __exit__(self, *exc) -> None:
        self.close()

    def close(self) -> None:
        self.conn.commit()
        self.conn.close()

    def log_run(self, stage: str, n_in: int, n_out: int, cost_usd: float = 0.0,
                notes: str = "") -> None:
        self.conn.execute(
            "INSERT INTO runs (run_date, stage, n_in, n_out, cost_usd, notes, created_at) "
            "VALUES (?,?,?,?,?,?,?)",
            (date.today().isoformat(), stage, n_in, n_out, cost_usd, notes,
             datetime.now().isoformat(timespec="seconds")),
        )
        self.conn.commit()
