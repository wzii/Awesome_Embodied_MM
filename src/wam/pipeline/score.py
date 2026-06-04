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


_TOP4 = {"generalist", "inference_speed", "specialist", "inference_cost"}


def weighted_total(card: ScoreCard, cfg: Config) -> float:
    """Excellence-oriented total: a paper that is outstanding on ONE WAM dimension scores high
    — it need not excel on all. WAM contribution is peak-dominant (max + top-k), not an
    average; general quality (novelty/soundness/impact) is a mean baseline. N/A is ignored."""
    s = cfg.get("scoring", {}) or {}
    gen_w = float(s.get("general_weight", 0.4))
    wam_w = float(s.get("wam_weight", 0.6))
    peak_w = float(s.get("wam_peak_weight", 0.6))   # within WAM: weight on the single best dim
    topk = int(s.get("wam_topk", 3))
    sec = float(s.get("secondary_discount", 0.8))   # non-top-4 WAM dims count a bit less

    gen = [v for v in vars(card.general).values() if isinstance(v, int)]
    gen_avg = sum(gen) / len(gen) if gen else 0.0

    wam = []
    for metric, v in vars(card.wam).items():
        if isinstance(v, int):
            wam.append(v if metric in _TOP4 else v * sec)
    if wam:
        wam.sort(reverse=True)
        peak = wam[0]
        top_mean = sum(wam[:topk]) / len(wam[:topk])
        wam_exc = peak_w * peak + (1 - peak_w) * top_mean
    else:
        wam_exc = gen_avg  # no WAM dims addressed → fall back to general quality
    return round(gen_w * gen_avg + wam_w * wam_exc, 2)


def run(cfg: Config, client: LLMClient, conn: sqlite3.Connection,
        limit: int | None = None) -> int:
    from wam.pipeline._concurrent import run_stage
    cap = limit or int(cfg.get("constants.analyze_cap", 40))
    system = SYSTEM.format(profile=cfg.profile_text())
    workers = int(cfg.get("constants.llm_workers", 6))
    # Fetch all needed text in the MAIN thread (workers must not touch the connection).
    todo = conn.execute(
        "SELECT id, title, abstract, summary_json, analysis_json FROM papers WHERE track='core' "
        "AND analysis_json IS NOT NULL AND scores_json IS NULL "
        "ORDER BY relevance DESC LIMIT ?", (cap,)).fetchall()
    log.info("scoring %d analyzed papers (%d workers)", len(todo), workers)

    def worker(row):
        ctx = (f"Title: {row['title']}\n\nAbstract: {row['abstract'] or '(none)'}\n\n"
               f"Summary: {row['summary_json']}\n\nAnalysis: {row['analysis_json']}")
        try:
            return row["id"], client.complete_json("score", system, ctx, ScoreCard,
                                                   label="score", max_tokens=5000)
        except Exception as e:  # noqa: BLE001
            log.warning("score failed for %s: %s", row["id"], e)
            return row["id"], None

    def store(pid, card):
        payload = card.model_dump()
        payload["weighted_total"] = weighted_total(card, cfg)
        ps.set_scores(conn, pid, json.dumps(payload))

    n = run_stage(todo, worker, store, conn, workers, "score", log)
    log.info("scored %d papers", n)
    return n
