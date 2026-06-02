"""Paper persistence: map ``PaperRecord`` <-> the ``papers`` table."""

from __future__ import annotations

import json
import sqlite3
from datetime import date, datetime

from wam.models import PaperRecord


def existing_ids(conn: sqlite3.Connection) -> set[str]:
    return {row["id"] for row in conn.execute("SELECT id FROM papers")}


def insert_new(conn: sqlite3.Connection, rec: PaperRecord, *, first_seen: str | None = None) -> None:
    """Insert a freshly-fetched record. No-op if the id already exists."""
    first_seen = first_seen or date.today().isoformat()
    conn.execute(
        """INSERT OR IGNORE INTO papers
           (id, source, title, authors_json, published, first_seen, abstract, categories_json,
            links_json, citations, influential_citations, has_code, status, updated_at)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (
            rec.id, rec.source, rec.title, json.dumps(rec.authors), rec.published, first_seen,
            rec.abstract, json.dumps(rec.categories), rec.links.model_dump_json(),
            rec.citations, rec.influential_citations, int(rec.has_code), "new",
            datetime.now().isoformat(timespec="seconds"),
        ),
    )


def update_enrichment(conn: sqlite3.Connection, rec: PaperRecord) -> None:
    """Refresh citation/code/link fields for an existing record (idempotent)."""
    conn.execute(
        """UPDATE papers SET citations=?, influential_citations=?, has_code=?, links_json=?,
           updated_at=? WHERE id=?""",
        (rec.citations, rec.influential_citations, int(rec.has_code), rec.links.model_dump_json(),
         datetime.now().isoformat(timespec="seconds"), rec.id),
    )


def count(conn: sqlite3.Connection) -> int:
    return conn.execute("SELECT count(*) AS c FROM papers").fetchone()["c"]
