"""Trends stage — popular research directions with momentum.

Clusters core+adjacent papers by embedding similarity (a cosine graph + greedy-modularity
communities), labels each direction with the strong model, and computes volume-over-time +
a rising/steady/cooling momentum signal (recent vs prior publication window). Results land in
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
from wam.store import index as idx

log = get_logger("pipeline.trends")


class FrontLabel(BaseModel):
    name: str = Field(description="a 4-8 word research-direction name")
    summary: str = Field(description="one sentence describing the direction")


def _month(d: str | None) -> str:
    return (d or "")[:7] or "unknown"


def _momentum(dates: list[str], window: int, today: date) -> str:
    recent = sum(1 for d in dates if d and date.fromisoformat(d) > today - timedelta(days=window))
    prior = sum(1 for d in dates if d and today - timedelta(days=2 * window)
                < date.fromisoformat(d) <= today - timedelta(days=window))
    if recent > prior * 1.3 and recent >= 2:
        return "rising"
    if recent < prior * 0.7:
        return "cooling"
    return "steady"


def run(cfg: Config, client: LLMClient, conn: sqlite3.Connection) -> int:
    import networkx as nx
    import numpy as np

    rows = conn.execute(
        "SELECT id, title, published, summary_json FROM papers WHERE track IN ('core','adjacent')"
    ).fetchall()
    if len(rows) < cfg.get("trends.min_front_size", 3):
        log.info("not enough papers for trends (%d)", len(rows))
        return 0
    texts = []
    for r in rows:
        tldr = json.loads(r["summary_json"] or "{}").get("tldr", "") if r["summary_json"] else ""
        texts.append(f"{r['title']}. {tldr}")
    log.info("embedding %d papers for trend clustering", len(rows))
    vecs = idx.embed_texts(cfg, texts)

    thr = float(cfg.get("trends.sim_threshold", 0.62))
    sims = vecs @ vecs.T
    g = nx.Graph()
    g.add_nodes_from(range(len(rows)))
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            if sims[i, j] >= thr:
                g.add_edge(i, j, weight=float(sims[i, j]))
    communities = nx.community.greedy_modularity_communities(g, weight="weight")

    today = date.today()
    window = int(cfg.get("trends.window_days", 30))
    min_size = int(cfg.get("trends.min_front_size", 3))
    snapshot = today.isoformat()
    conn.execute("DELETE FROM fronts WHERE snapshot_date=?", (snapshot,))
    n_fronts = 0
    for ci, comm in enumerate(communities):
        members = [rows[i] for i in comm]
        if len(members) < min_size:
            continue
        titles = "\n".join(f"- {m['title']}" for m in members[:12])
        try:
            label = client.complete_json(
                "strong", "Name the shared research direction of these WAM-related papers.",
                titles, FrontLabel, label="front-label", max_tokens=1500)
            name, summary = label.name, label.summary
        except Exception as e:  # noqa: BLE001
            log.warning("front label failed: %s", e)
            name, summary = f"Direction {ci+1}", ""
        dates = [m["published"] for m in members]
        volume = dict(Counter(_month(d) for d in dates))
        mom = _momentum(dates, window, today)
        conn.execute(
            "INSERT INTO fronts (front_id, snapshot_date, name, summary, member_ids_json, "
            "size, momentum, volume_json) VALUES (?,?,?,?,?,?,?,?)",
            (f"front-{ci}", snapshot, name, summary, json.dumps([m["id"] for m in members]),
             len(members), mom, json.dumps(volume)))
        n_fronts += 1
    conn.commit()
    log.info("stored %d research fronts (snapshot %s)", n_fronts, snapshot)
    return n_fronts
