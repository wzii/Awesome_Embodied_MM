"""Score stage — two-layer WAM rubric for core papers (strong tier).

Produces ``scores_json = {general, wam, weighted_total, rationale}``. The weighted total is
computed over *available* (non-"N/A") metrics using config weights; the top-4 WAM metrics are
weighted 2x by default so they dominate. Capped at ``constants.analyze_cap`` per run.
"""

from __future__ import annotations

import json
import sqlite3

from wam.config import Config
from wam.llm import LLMClient
from wam.logging import get_logger
from wam.pipeline.schemas import ScoreCard
from wam.store import papers as ps

log = get_logger("pipeline.score")

SYSTEM = ("Score the paper on the two-layer WAM rubric. Use the profile's definitions and "
          "scoring guidance. Output 0-10 per metric, or \"N/A\" when the paper does not address "
          "a metric (do NOT guess). Be skeptical of self-reported numbers. Write the "
          "rationale in English.\n\n"
          "--- PROFILE ---\n{profile}")


def weighted_total(card: ScoreCard, cfg: Config) -> float:
    gw = cfg.get("scoring.general_weights", {}) or {}
    ww = cfg.get("scoring.wam_weights", {}) or {}
    num = den = 0.0
    for metric, weight in gw.items():
        v = getattr(card.general, metric, "N/A")
        if isinstance(v, int):
            num += weight * v
            den += weight
    for metric, weight in ww.items():
        v = getattr(card.wam, metric, "N/A")
        if isinstance(v, int):
            num += weight * v
            den += weight
    return round(num / den, 2) if den else 0.0


def run(cfg: Config, client: LLMClient, conn: sqlite3.Connection,
        limit: int | None = None) -> int:
    cap = limit or int(cfg.get("constants.analyze_cap", 40))
    system = SYSTEM.format(profile=cfg.profile_text())
    todo = ps.needs_score(conn, limit=cap)
    log.info("scoring %d analyzed papers (cap=%d)", len(todo), cap)
    done = 0
    for row in todo:
        analysis = conn.execute("SELECT summary_json, analysis_json FROM papers WHERE id=?",
                                (row["id"],)).fetchone()
        ctx = (f"Title: {row['title']}\n\nAbstract: {row['abstract'] or '(none)'}\n\n"
               f"Summary: {analysis['summary_json']}\n\nAnalysis: {analysis['analysis_json']}")
        try:
            card = client.complete_json("score", system, ctx, ScoreCard,
                                        label="score", max_tokens=5000)
        except Exception as e:  # noqa: BLE001
            log.warning("score failed for %s: %s", row["id"], e)
            continue
        payload = card.model_dump()
        payload["weighted_total"] = weighted_total(card, cfg)
        ps.set_scores(conn, row["id"], json.dumps(payload))
        done += 1
        if done % 10 == 0:
            conn.commit()
    conn.commit()
    log.info("scored %d papers", done)
    return done
