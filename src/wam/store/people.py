"""Authors + groups persistence."""

from __future__ import annotations

import json
import re
import sqlite3
from datetime import datetime


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def upsert_author(conn: sqlite3.Connection, *, author_id: str, name: str,
                  affiliation: str | None, s2_url: str | None, citations: int | None,
                  h_index: int | None, paper_ids: list[str], directions: str | None) -> None:
    conn.execute(
        """INSERT INTO authors
           (id, name, affiliation, s2_url, citations, h_index, paper_ids_json, directions,
            updated_at)
           VALUES (?,?,?,?,?,?,?,?,?)
           ON CONFLICT(id) DO UPDATE SET
             affiliation=COALESCE(excluded.affiliation, affiliation),
             s2_url=COALESCE(excluded.s2_url, s2_url),
             citations=COALESCE(excluded.citations, citations),
             h_index=COALESCE(excluded.h_index, h_index),
             paper_ids_json=excluded.paper_ids_json,
             directions=COALESCE(excluded.directions, directions),
             updated_at=excluded.updated_at""",
        (author_id, name, affiliation, s2_url, citations, h_index, json.dumps(paper_ids),
         directions, datetime.now().isoformat(timespec="seconds")),
    )


def upsert_group(conn: sqlite3.Connection, *, group_id: str, name: str,
                 affiliation: str | None, member_ids: list[str], directions: str | None,
                 notable: list[str]) -> None:
    conn.execute(
        """INSERT INTO groups (id, name, affiliation, member_ids_json, directions,
            notable_json, updated_at)
           VALUES (?,?,?,?,?,?,?)
           ON CONFLICT(id) DO UPDATE SET
             member_ids_json=excluded.member_ids_json,
             directions=COALESCE(excluded.directions, directions),
             notable_json=excluded.notable_json,
             updated_at=excluded.updated_at""",
        (group_id, name, affiliation, json.dumps(member_ids), directions, json.dumps(notable),
         datetime.now().isoformat(timespec="seconds")),
    )
