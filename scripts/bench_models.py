#!/usr/bin/env python3
"""Generate anonymized model outputs for a BLIND ranking.

We do NOT score here. Each candidate model runs the representative tasks on a few real
papers; outputs are written under anonymized codes (M01..) with a private label map. A
separate strong, high-reasoning ranker (Opus 4.8) then ranks the codes WITHOUT seeing model
names — avoiding both judge saturation and brand bias. Costs/latencies are pure generation
(no judge), so they're accurate per-model.

    python scripts/bench_models.py --papers 3 --out /tmp/wam_rank

Writes <out>/anon_outputs.json (given to the ranker), <out>/label_map.json and
<out>/stats.json (kept private, for de-anonymizing after).
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from wam.config import load_config  # noqa: E402
from wam.llm import LLMClient  # noqa: E402
from wam.logging import COST, get_logger, setup_logging  # noqa: E402
from wam.pipeline.schemas import PaperSummary, ScoreCard  # noqa: E402
from wam.store import Database  # noqa: E402

log = get_logger("bench")

# Latest small + large model from each major family (live OpenRouter catalog, current
# versions only). Edit freely.
MODELS = [
    "openai/gpt-5.4-nano", "openai/gpt-5.4-mini",
    "google/gemini-3.1-flash-lite", "google/gemini-3.5-flash",
    "anthropic/claude-haiku-4.5", "anthropic/claude-sonnet-4.6",
    "deepseek/deepseek-v4-flash", "deepseek/deepseek-v4-pro",
    "z-ai/glm-4.7-flash", "z-ai/glm-5.1",
    "qwen/qwen3.6-flash", "qwen/qwen3.7-max",
    "moonshotai/kimi-k2.6",
    "xiaomi/mimo-v2.5", "xiaomi/mimo-v2.5-pro",
]

TASKS = {
    "summary": (PaperSummary, "Summarize this paper: one-sentence tldr, problem, method, "
                              "results."),
    "score": (ScoreCard, "Score this paper on the two-layer WAM rubric (general: novelty/"
                         "soundness/impact; wam: generalist/inference_speed/specialist/"
                         "inference_cost/trustworthiness/collaborative/controlled_generation/"
                         "other), each 0-10 or \"N/A\", with a brief rationale."),
}


def live_pricing(ids: list[str]) -> dict[str, dict[str, float]]:
    data = requests.get("https://openrouter.ai/api/v1/models", timeout=60).json()["data"]
    out = {}
    for m in data:
        if m["id"] in ids:
            p = m.get("pricing", {})
            out[m["id"]] = {"input": float(p.get("prompt", 0)) * 1e6,
                            "output": float(p.get("completion", 0)) * 1e6}
    return out


def sample_papers(db: Database, n: int) -> list[dict]:
    rows = db.conn.execute(
        "SELECT id, title, abstract FROM papers WHERE source='arxiv' AND abstract IS NOT NULL "
        "ORDER BY length(abstract) DESC LIMIT ?", (n,)).fetchall()
    return [dict(r) for r in rows]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--papers", type=int, default=3)
    ap.add_argument("--out", default="/tmp/wam_rank")
    ap.add_argument("--models", nargs="*")
    args = ap.parse_args()

    cfg = load_config()
    setup_logging(level="INFO", debug=True)
    cfg.require_env(cfg.get("provider.api_key_env"))
    models = args.models or MODELS
    cfg.data.setdefault("models", {})["cost_per_million"] = live_pricing(models)
    profile = cfg.profile_text()
    client = LLMClient(cfg)

    with Database(cfg) as db:
        papers = sample_papers(db, args.papers)
    log.info("generating outputs for %d models on %d papers x %d tasks",
             len(models), len(papers), len(TASKS))

    # Anonymize: shuffle so code order != model order; codes carry no brand info.
    rng = random.Random(1234)
    shuffled = models[:]
    rng.shuffle(shuffled)
    code_of = {m: f"M{ix:02d}" for ix, m in enumerate(shuffled, 1)}

    # anon[task][paper_idx][code] = output ; papers_meta[paper_idx] = {title, abstract}
    anon: dict = {t: {} for t in TASKS}
    papers_meta = {str(i): {"title": p["title"], "abstract": p["abstract"]}
                   for i, p in enumerate(papers)}
    stats: dict = {}

    for model in models:
        c0 = COST.cost_usd
        lats, n_ok = [], 0
        for i, p in enumerate(papers):
            for tname, (schema, task) in TASKS.items():
                user = f"Paper: {p['title']}\n\nAbstract: {p['abstract']}\n\nTask: {task}"
                t0 = time.monotonic()
                try:
                    obj = client.complete_json("mid", profile, user, schema, model=model,
                                               label=f"{model}:{tname}", max_tokens=8000)
                except Exception as e:  # noqa: BLE001
                    log.warning("%s failed (%s) p%d: %s", model, tname, i, e)
                    continue
                lats.append(time.monotonic() - t0)
                n_ok += 1
                anon[tname].setdefault(str(i), {})[code_of[model]] = obj.model_dump()
        stats[model] = {
            "code": code_of[model], "cost_gen": round(COST.cost_usd - c0, 5),
            "mean_latency_s": round(sum(lats) / len(lats), 2) if lats else None,
            "n_ok": n_ok, "n_expected": len(papers) * len(TASKS),
        }
        log.info("  %-32s code=%s cost=$%.5f lat=%ss ok=%d/%d", model,
                 code_of[model], stats[model]["cost_gen"], stats[model]["mean_latency_s"],
                 n_ok, stats[model]["n_expected"])

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "anon_outputs.json").write_text(json.dumps({"papers": papers_meta, "tasks": anon},
                                                      indent=2))
    (out / "label_map.json").write_text(json.dumps({v: k for k, v in code_of.items()}, indent=2))
    (out / "stats.json").write_text(json.dumps(stats, indent=2))
    log.info("wrote anon outputs + private maps to %s", out)
    log.info(COST.summary())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
