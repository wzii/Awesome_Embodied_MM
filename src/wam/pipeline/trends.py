"""Trends stage — popular research directions with momentum (long-context, no embeddings).

Feeds the full list of tracked papers (id + title + tldr) to a strong long-context model and
asks it to cluster them into research directions. Momentum (rising/steady/cooling) is then
computed in code from members' publication dates (recent vs prior window). Results land in
the ``fronts`` table and render into the README.
"""

from __future__ import annotations

import json
import sqlite3
from collections import Counter
from datetime import date, datetime, timedelta

from pydantic import BaseModel, Field

from wam.config import Config
from wam.llm import LLMClient
from wam.logging import get_logger

log = get_logger("pipeline.trends")


class Direction(BaseModel):
    name: str = Field(description="a 4-8 word research-direction name")
    summary: str = Field(description="one sentence describing the direction")
    members: list[int] = Field(description="indices (from the numbered list) of papers in it")


class TrendResult(BaseModel):
    directions: list[Direction]


SYSTEM = ("Cluster these World Action Models papers into coherent research directions "
          "(aim for 6-12 directions). Every paper index should belong to exactly one "
          "direction; put genuine outliers in a 'Miscellaneous' direction. Use the numbered "
          "list; refer to papers only by their index. Write direction names and summaries in "
          "English.")


def _month(d: str | None) -> str:
    return (d or "")[:7] or "unknown"


def _momentum(dates: list[str], window: int, today: date) -> str:
    def n_between(lo, hi):
        c = 0
        for d in dates:
            if not d:
                continue
            try:
                dd = date.fromisoformat(d)
            except ValueError:
                continue
            if lo < dd <= hi:
                c += 1
        return c
    recent = n_between(today - timedelta(days=window), today)
    prior = n_between(today - timedelta(days=2 * window), today - timedelta(days=window))
    if recent > prior * 1.3 and recent >= 2:
        return "rising"
    if recent < prior * 0.7:
        return "cooling"
    return "steady"


def run(cfg: Config, client: LLMClient, conn: sqlite3.Connection) -> int:
    rows = conn.execute(
        "SELECT id, title, published, summary_json FROM papers WHERE track IN ('core','adjacent') "
        "ORDER BY published DESC").fetchall()
    min_size = int(cfg.get("trends.min_front_size", 3))
    if len(rows) < min_size:
        log.info("not enough papers for trends (%d)", len(rows))
        return 0

    lines = []
    for i, r in enumerate(rows):
        tldr = json.loads(r["summary_json"] or "{}").get("tldr", "") if r["summary_json"] else ""
        lines.append(f"{i}. {r['title']} — {tldr}")
    log.info("clustering %d papers into directions (long-context)", len(rows))
    # Clustering 200+ papers is a large-output task: use the fast, JSON-reliable cheap model
    # (glm-5.1 was too slow here and truncated). Generous token ceiling for the index lists.
    res = client.complete_json("cheap", SYSTEM, "\n".join(lines), TrendResult,
                               label="trends", max_tokens=12000)
    log.info("model returned %d directions, member counts: %s", len(res.directions),
             [len(d.members) for d in res.directions])

    today = date.today()
    window = int(cfg.get("trends.window_days", 30))
    snapshot = today.isoformat()
    conn.execute("DELETE FROM fronts WHERE snapshot_date=?", (snapshot,))
    n = 0
    for ci, d in enumerate(res.directions):
        members = [rows[i] for i in d.members if 0 <= i < len(rows)]
        if len(members) < min_size:
            continue
        dates = [m["published"] for m in members]
        conn.execute(
            "INSERT INTO fronts (front_id, snapshot_date, name, summary, member_ids_json, "
            "size, momentum, volume_json) VALUES (?,?,?,?,?,?,?,?)",
            (f"front-{ci}", snapshot, d.name, d.summary,
             json.dumps([m["id"] for m in members]), len(members),
             _momentum(dates, window, today), json.dumps(dict(Counter(_month(x) for x in dates)))))
        n += 1
    conn.commit()
    log.info("stored %d research fronts (snapshot %s)", n, snapshot)
    return n
