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


# --- stage work-queues -------------------------------------------------------
# Each returns rows (id, title, abstract, ...) that still need a given stage. Relevance
# acts as a cache: a paper with track already set is not re-filtered.

def _rows(conn: sqlite3.Connection, where: str, params: tuple = ()) -> list[sqlite3.Row]:
    return conn.execute(
        f"SELECT id, source, title, abstract, published, categories_json FROM papers "
        f"WHERE {where}", params).fetchall()


def _limit_clause(where: str, limit: int | None) -> str:
    return where + (f" LIMIT {int(limit)}" if limit else "")


def needs_filter(conn: sqlite3.Connection, limit: int | None = None) -> list[sqlite3.Row]:
    # track NULL = unfiltered; relevance=-1 = a prior failure to retry.
    return _rows(conn, _limit_clause("track IS NULL OR relevance = -1", limit))


def needs_summary(conn: sqlite3.Connection, limit: int | None = None) -> list[sqlite3.Row]:
    return _rows(conn, _limit_clause(
        "track IN ('core','adjacent') AND summary_json IS NULL", limit))


def needs_analysis(conn: sqlite3.Connection, limit: int | None = None) -> list[sqlite3.Row]:
    q = "track = 'core' AND analysis_json IS NULL"
    if limit:
        q += f" ORDER BY relevance DESC LIMIT {int(limit)}"
    return _rows(conn, q)


def needs_score(conn: sqlite3.Connection, limit: int | None = None) -> list[sqlite3.Row]:
    q = "track = 'core' AND analysis_json IS NOT NULL AND scores_json IS NULL"
    if limit:
        q += f" ORDER BY relevance DESC LIMIT {int(limit)}"
    return _rows(conn, q)


def needs_innovation(conn: sqlite3.Connection, limit: int | None = None) -> list[sqlite3.Row]:
    return _rows(conn, _limit_clause("track = 'adjacent' AND innovation_json IS NULL", limit))


def needs_extract(conn: sqlite3.Connection, limit: int | None = None) -> list[sqlite3.Row]:
    # core + adjacent papers not yet benchmark-extracted (VLA/world-model papers report
    # standard embodied benchmarks too). No analysis requirement — extraction reads the PDF.
    return conn.execute(_limit_clause(
        "SELECT id, source, title, abstract, links_json FROM papers WHERE "
        "track IN ('core','adjacent') AND benchmarks_extracted=0", limit)).fetchall()


def needs_institute(conn: sqlite3.Connection, limit: int | None = None) -> list[sqlite3.Row]:
    # core + adjacent papers whose author affiliations haven't been extracted yet.
    return conn.execute(_limit_clause(
        "SELECT id, source, title, abstract, links_json FROM papers WHERE "
        "track IN ('core','adjacent') AND institutes_extracted=0", limit)).fetchall()


# --- stage writers -----------------------------------------------------------
def _touch(conn: sqlite3.Connection, pid: str, **cols) -> None:
    cols["updated_at"] = datetime.now().isoformat(timespec="seconds")
    sets = ", ".join(f"{k}=?" for k in cols)
    conn.execute(f"UPDATE papers SET {sets} WHERE id=?", (*cols.values(), pid))


def set_filter(conn, pid: str, track: str, relevance: float, reason: str) -> None:
    _touch(conn, pid, track=track, relevance=relevance, relevance_reason=reason,
           status="filtered")


def set_summary(conn, pid: str, summary_json: str) -> None:
    _touch(conn, pid, summary_json=summary_json, status="summarized")


def set_analysis(conn, pid: str, analysis_json: str) -> None:
    _touch(conn, pid, analysis_json=analysis_json, status="analyzed")


def set_scores(conn, pid: str, scores_json: str) -> None:
    _touch(conn, pid, scores_json=scores_json, status="scored")


def set_innovation(conn, pid: str, innovation_json: str) -> None:
    _touch(conn, pid, innovation_json=innovation_json, status="done")


def set_institutes(conn, pid: str, institutes_json: str) -> None:
    _touch(conn, pid, institutes_json=institutes_json, institutes_extracted=1)
