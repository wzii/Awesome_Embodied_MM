"""People stage — influential authors + research groups.

Identity comes from **Semantic Scholar author IDs** attached to each paper (reliable; avoids
name collisions), not name search. Influential authors (on >= N tracked papers) get an
LLM-summarized research direction. **Groups are co-authorship clusters**: influential authors
who publish together form a lab/group (connected components of the co-authorship graph) —
this works even though S2's affiliation data is sparse.
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


class AuthorProfile(BaseModel):
    directions: str = Field(description="1-2 sentences on this author's main WAM-related "
                                        "research directions, grounded in the listed papers")
    affiliation: str | None = Field(default=None, description="the author's institution as "
                                    "stated in the papers' author/affiliation block, else null")
    region: str | None = Field(default=None, description="country/region of that institution "
                               "(e.g. 'China', 'USA', 'Singapore'), else null")


def run(cfg: Config, client: LLMClient, conn: sqlite3.Connection,
        limit: int | None = None) -> dict[str, int]:
    min_papers = int(cfg.get("people.min_papers", 2))
    cap = limit or int(cfg.get("people.max_per_run", 30))

    rows = conn.execute(
        "SELECT id, title, summary_json FROM papers WHERE track IN ('core','adjacent')").fetchall()
    meta = {r["id"]: {"title": r["title"],
                      "tldr": (json.loads(r["summary_json"] or "{}").get("tldr", "")
                               if r["summary_json"] else "")} for r in rows}
    arxiv_ids = [r["id"].split("arxiv:", 1)[1] for r in rows if r["id"].startswith("arxiv:")]
    authors_by_paper = s2.fetch_authors(cfg, arxiv_ids)
    log.info("got authors for %d papers", len(authors_by_paper))
    if not authors_by_paper:
        # Don't wipe the existing registry on a transient S2 failure (e.g. 429).
        log.warning("no author data from S2 (rate-limited?); keeping existing registry")
        return {"authors": 0, "groups": 0}

    # Aggregate by S2 authorId.
    agg: dict[str, dict] = {}
    for pid, alist in authors_by_paper.items():
        for a in alist:
            aid = a.get("authorId")
            if not aid:
                continue
            e = agg.setdefault(aid, {"name": a.get("name") or "?", "pids": set(),
                                     "affiliation": None, "h_index": a.get("hIndex"),
                                     "citations": a.get("citationCount")})
            e["pids"].add(pid)
            affs = a.get("affiliations") or []
            if affs and not e["affiliation"]:
                e["affiliation"] = affs[0]

    influential = {aid: e for aid, e in agg.items() if len(e["pids"]) >= min_papers}
    ranked = sorted(influential, key=lambda x: -len(influential[x]["pids"]))[:cap]
    log.info("%d distinct S2 authors; %d influential (>=%d papers); processing top %d",
             len(agg), len(influential), min_papers, len(ranked))

    # Fresh rebuild each run.
    conn.execute("DELETE FROM authors")
    conn.execute("DELETE FROM groups")

    from wam.sources import pdf
    kept = set(ranked)
    for aid in ranked:
        e = influential[aid]
        titles = "\n".join(f"- {meta[p]['title']}: {meta[p]['tldr']}" for p in e["pids"]
                           if p in meta)
        # Author/affiliation block lives on the PDF first page — give the model that text
        # (cached only, no download) so institution + region are grounded, not guessed.
        blocks = []
        for p in sorted(e["pids"])[:2]:
            txt = pdf.get_text(cfg, p, "", max_chars=2500)
            if txt:
                blocks.append(f"[{meta.get(p,{}).get('title','')}]\n{txt}")
        ctx = (f"Author: {e['name']}\nTracked papers:\n{titles}\n\n"
               f"Author/affiliation blocks (first pages):\n" + "\n---\n".join(blocks))
        aff, region, directions = e["affiliation"], None, None
        try:
            prof = client.complete_json(
                "cheap", "For the given author, summarize their WAM research directions and, "
                "FROM the author/affiliation blocks only, extract their institution and "
                "country/region. If a field isn't in the text, use null. Write in English.",
                ctx, AuthorProfile, label="author-profile", max_tokens=2000)
            directions = prof.directions
            aff = prof.affiliation or e["affiliation"]
            region = prof.region
        except Exception as ex:  # noqa: BLE001
            log.warning("profile failed for %s: %s", e["name"], ex)
        store.upsert_author(
            conn, author_id=aid, name=e["name"], affiliation=aff, region=region,
            s2_url=f"https://www.semanticscholar.org/author/{aid}", citations=e["citations"],
            h_index=e["h_index"], paper_ids=sorted(e["pids"]), directions=directions)
    conn.commit()

    # Groups = co-authorship clusters among the influential authors.
    import networkx as nx
    g = nx.Graph()
    g.add_nodes_from(kept)
    for pid, alist in authors_by_paper.items():
        ids = [a["authorId"] for a in alist if a.get("authorId") in kept]
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                g.add_edge(ids[i], ids[j])
    n_grp = 0
    for comp in nx.connected_components(g):
        members = [m for m in comp]
        if len(members) < 2:
            continue
        lead = max(members, key=lambda m: len(influential[m]["pids"]))
        aff = next((influential[m]["affiliation"] for m in members
                    if influential[m]["affiliation"]), None)
        name = f"{influential[lead]['name']} group" + (f" · {aff}" if aff else "")
        notable = sorted({p for m in members for p in influential[m]["pids"]})[:8]
        store.upsert_group(conn, group_id=slug(name), name=name, affiliation=aff,
                           member_ids=members, directions=None, notable=notable)
        n_grp += 1
    conn.commit()
    log.info("stored %d authors, %d co-authorship groups", len(ranked), n_grp)
    return {"authors": len(ranked), "groups": n_grp}
