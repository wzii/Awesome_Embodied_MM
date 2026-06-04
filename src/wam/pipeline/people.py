"""People stage — influential authors + research groups.

Aggregates authors across tracked (core + adjacent) papers, flags the influential ones
(appear on >= N tracked papers, or high Semantic Scholar citations), enriches them via S2
(affiliation, citations, h-index), and uses the strong model to summarize each one's main
research directions. Groups are inferred from shared affiliation among influential authors.
"""

from __future__ import annotations

import json
import sqlite3
from collections import defaultdict

from pydantic import BaseModel, Field

from wam.config import Config
from wam.llm import LLMClient
from wam.logging import get_logger
from wam.sources import semantic_scholar as s2
from wam.store import people as store
from wam.store.people import slug

log = get_logger("pipeline.people")


class Directions(BaseModel):
    directions: str = Field(description="1-2 sentences on this author's main WAM-related "
                                        "research directions, grounded in the listed papers")


def _tracked_authorship(conn: sqlite3.Connection) -> tuple[dict, dict]:
    """Return (author_name -> [paper_ids], paper_id -> {title, tldr})."""
    rows = conn.execute(
        "SELECT id, title, authors_json, summary_json FROM papers "
        "WHERE track IN ('core','adjacent')").fetchall()
    by_author: dict[str, list[str]] = defaultdict(list)
    papers: dict[str, dict] = {}
    for r in rows:
        tldr = ""
        if r["summary_json"]:
            try:
                tldr = json.loads(r["summary_json"]).get("tldr", "")
            except Exception:  # noqa: BLE001
                pass
        papers[r["id"]] = {"title": r["title"], "tldr": tldr}
        for name in json.loads(r["authors_json"] or "[]"):
            if name and name != "(none)":
                by_author[name].append(r["id"])
    return by_author, papers


def run(cfg: Config, client: LLMClient, conn: sqlite3.Connection,
        limit: int | None = None) -> dict[str, int]:
    min_papers = int(cfg.get("people.min_papers", 2))
    cap = limit or int(cfg.get("people.max_per_run", 30))
    by_author, papers = _tracked_authorship(conn)
    log.info("aggregated %d distinct authors across tracked papers", len(by_author))

    # Process the most prolific authors first, bounded per run to keep cost/time sane.
    candidates = sorted(((n, p) for n, p in by_author.items() if len(p) >= min_papers),
                        key=lambda kv: -len(kv[1]))[:cap]
    influential: dict[str, dict] = {}
    for name, pids in candidates:
        influential[name] = {"pids": pids, "s2": s2.search_author(cfg, name)}

    log.info("identified %d influential authors (processing top %d)", len(candidates), cap)
    n_auth = 0
    for name, info in influential.items():
        titles = "\n".join(f"- {papers[p]['title']}: {papers[p]['tldr']}" for p in info["pids"]
                           if p in papers)
        try:
            d = client.complete_json(
                "cheap", "Summarize an author's research directions for a WAM digest. Write "
                "in English.",
                f"Author: {name}\nTheir tracked papers:\n{titles}", Directions,
                label="author-directions", max_tokens=2000).directions
        except Exception as e:  # noqa: BLE001
            log.warning("directions failed for %s: %s", name, e)
            d = None
        s2info = info["s2"] or {}
        store.upsert_author(
            conn, author_id=s2info.get("id") or slug(name), name=name,
            affiliation=s2info.get("affiliation"), s2_url=s2info.get("url"),
            citations=s2info.get("citations"), h_index=s2info.get("h_index"),
            paper_ids=info["pids"], directions=d)
        n_auth += 1
    conn.commit()

    # Groups by shared affiliation among influential authors.
    by_aff: dict[str, list[str]] = defaultdict(list)
    for name, info in influential.items():
        aff = (info["s2"] or {}).get("affiliation")
        if aff:
            by_aff[aff].append(name)
    n_grp = 0
    for aff, members in by_aff.items():
        if len(members) < 2:
            continue
        member_ids = [slug(m) for m in members]
        notable = sorted({p for m in members for p in influential[m]["pids"]})[:8]
        store.upsert_group(conn, group_id=slug(aff), name=aff, affiliation=aff,
                           member_ids=member_ids, directions=None, notable=notable)
        n_grp += 1
    conn.commit()
    log.info("stored %d authors, %d groups", n_auth, n_grp)
    return {"authors": n_auth, "groups": n_grp}
