#!/usr/bin/env python3
"""Empirically pick tier models: run candidates on real papers, judge quality vs price.

For each tier, every candidate model runs the tier's representative task on a few real
papers from the DB; an independent judge model rates each output 0-10. We report mean
quality, total cost (live OpenRouter pricing), mean latency, and a quality-per-dollar
ranking so the choice is data-driven rather than guessed.

    python scripts/bench_models.py --tier all --papers 3
    python scripts/bench_models.py --tier cheap --judge google/gemini-2.5-pro

Needs OPENROUTER_API_KEY. Spend is small (cheap models, few papers) but nonzero.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pydantic import BaseModel, Field  # noqa: E402

from wam.config import load_config  # noqa: E402
from wam.llm import LLMClient  # noqa: E402
from wam.logging import COST, get_logger, setup_logging  # noqa: E402
from wam.pipeline.schemas import PaperAnalysis, PaperSummary, RelevanceVerdict, ScoreCard  # noqa: E402
from wam.store import Database  # noqa: E402

log = get_logger("bench")

# Candidate models per tier (from the live OpenRouter catalog; edit freely).
CANDIDATES = {
    "cheap":  ["deepseek/deepseek-v4-flash", "google/gemini-2.5-flash-lite",
               "openai/gpt-5-nano", "openai/gpt-oss-120b"],
    "mid":    ["deepseek/deepseek-v4-pro", "google/gemini-3-flash-preview",
               "openai/gpt-5-mini", "anthropic/claude-haiku-4.5"],
    "strong": ["deepseek/deepseek-v4-pro", "google/gemini-3.5-flash",
               "google/gemini-2.5-pro", "anthropic/claude-sonnet-4.6"],
}
DEFAULT_JUDGE = "anthropic/claude-sonnet-4.6"

# Tier -> (schema, task description used in the prompt)
TASKS = {
    "cheap":  (RelevanceVerdict, "Classify this paper's track (core/adjacent/drop for World "
                                 "Action Models) and give a 0-1 relevance with one reason."),
    "mid":    (PaperAnalysis, "Give a deep technical analysis: contributions, limitations, and "
                              "why it matters for World Action Models."),
    "strong": (ScoreCard, "Score this paper on the two-layer WAM rubric (general + WAM "
                          "metrics, 0-10 or N/A) with a brief rationale."),
}


class Quality(BaseModel):
    quality: int = Field(ge=0, le=10, description="0-10 faithfulness+usefulness of the output")
    note: str


def live_pricing(candidate_ids: list[str]) -> dict[str, dict[str, float]]:
    data = requests.get("https://openrouter.ai/api/v1/models", timeout=60).json()["data"]
    out = {}
    for m in data:
        if m["id"] in candidate_ids:
            p = m.get("pricing", {})
            out[m["id"]] = {"input": float(p.get("prompt", 0)) * 1e6,
                            "output": float(p.get("completion", 0)) * 1e6}
    return out


def sample_papers(db: Database, n: int) -> list[dict]:
    rows = db.conn.execute(
        "SELECT id, title, abstract FROM papers WHERE source='arxiv' AND abstract IS NOT NULL "
        "ORDER BY length(abstract) DESC LIMIT ?", (n,)).fetchall()
    return [dict(r) for r in rows]


def run_tier(client: LLMClient, tier: str, papers: list[dict], judge: str) -> list[dict]:
    schema, task = TASKS[tier]
    profile = client.cfg.profile_text()
    results = []
    for model in CANDIDATES[tier]:
        cost0, in0, out0 = COST.cost_usd, COST.input_tokens, COST.output_tokens
        lat, quals, outputs = [], [], []
        for p in papers:
            user = f"Paper: {p['title']}\n\nAbstract: {p['abstract']}\n\nTask: {task}"
            t0 = time.monotonic()
            try:
                obj = client.complete_json("mid", profile, user, schema, model=model,
                                           label=f"{tier}:{model}", max_tokens=1500)
            except Exception as e:  # noqa: BLE001
                log.warning("%s failed on %s: %s", model, p["id"], e)
                continue
            lat.append(time.monotonic() - t0)
            outputs.append(obj.model_dump())
            # judge
            try:
                q = client.complete_json(
                    "strong", "You are a strict reviewer judging the quality of an automated "
                    "analysis of a paper. Rate 0-10 for faithfulness to the abstract and "
                    "usefulness.", f"Abstract: {p['abstract']}\n\nModel output:\n{obj.model_dump()}",
                    Quality, model=judge, label="judge", max_tokens=300)
                quals.append(q.quality)
            except Exception as e:  # noqa: BLE001
                log.warning("judge failed: %s", e)
        dcost = COST.cost_usd - cost0
        results.append({
            "model": model,
            "mean_quality": round(sum(quals) / len(quals), 2) if quals else None,
            "cost_for_run": round(dcost, 5),
            "mean_latency_s": round(sum(lat) / len(lat), 2) if lat else None,
            "tokens": (COST.input_tokens - in0, COST.output_tokens - out0),
            "n_ok": len(outputs),
        })
        log.info("  %-40s q=%s cost=$%.5f lat=%.2fs", model,
                 results[-1]["mean_quality"], dcost, results[-1]["mean_latency_s"] or 0)
    return results


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", choices=["cheap", "mid", "strong", "all"], default="all")
    ap.add_argument("--papers", type=int, default=3)
    ap.add_argument("--judge", default=DEFAULT_JUDGE)
    args = ap.parse_args()

    cfg = load_config()
    setup_logging(level="INFO", debug=True)  # full trace to logs/
    cfg.require_env(cfg.get("provider.api_key_env"))

    tiers = ["cheap", "mid", "strong"] if args.tier == "all" else [args.tier]
    all_ids = sorted({m for t in tiers for m in CANDIDATES[t]} | {args.judge})
    cfg.data.setdefault("models", {})["cost_per_million"] = live_pricing(all_ids)
    log.info("loaded live pricing for %d models", len(cfg.get("models.cost_per_million")))

    client = LLMClient(cfg)
    with Database(cfg) as db:
        papers = sample_papers(db, args.papers)
    log.info("benchmarking on %d papers, judge=%s", len(papers), args.judge)

    report = {}
    for tier in tiers:
        log.info("=== tier: %s ===", tier)
        report[tier] = run_tier(client, tier, papers, args.judge)

    print("\n================ RESULTS ================")
    for tier, rows in report.items():
        print(f"\n[{tier}]  (quality 0-10, cost for {len(papers)} papers)")
        rows = [r for r in rows if r["mean_quality"] is not None]
        for r in sorted(rows, key=lambda x: (-x["mean_quality"], x["cost_for_run"])):
            qpd = r["mean_quality"] / r["cost_for_run"] if r["cost_for_run"] else float("inf")
            print(f"  {r['model']:42s} q={r['mean_quality']:<5} ${r['cost_for_run']:<9.5f} "
                  f"{r['mean_latency_s']}s  q/$={qpd:.0f}")
    print(f"\n{COST.summary()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
