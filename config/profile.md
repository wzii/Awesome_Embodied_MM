# WAM Research Interest Profile

This profile is read verbatim by the relevance-filter and scoring prompts. It defines
what "World Action Models" means for this project and what we care about. Edit freely —
no code changes needed.

## What counts as a World Action Model (WAM)

A WAM is a learned model that maps perception + goals to **actions** in the physical or
simulated world, often grounded in a learned **world model** (predictive dynamics). The
umbrella includes:

- Generalist robot/agent policies and embodied foundation models
- Vision-Language-Action (VLA) models that output actions
- World models / action-conditioned video & dynamics models used for planning or control
- Models that unify perception, prediction, and action for embodied agents

## Two relevance tracks

- **core** — the paper *is* a WAM (or directly proposes/evaluates one). Gets the full
  two-layer rubric and benchmark extraction.
- **adjacent** — VLA / world model / video-generation work that is *not* a WAM itself but
  carries a technique plausibly **transferable to WAM**. Gets an innovation note only
  (key idea + why it could transfer); no rubric scores.
- **drop** — unrelated to the above.

## What we care most about (drives WAM-specific scoring)

Top-4 (weighted 2x):
1. **inference_speed** — real-time or faster control; latency/throughput on stated hardware.
2. **generalist** — generalizes across tasks, benchmarks, and especially *embodiments*.
3. **specialist** — extreme accuracy/robustness on a specific task or task set.
4. **inference_cost** — compute/$ to run; small models that punch above their weight.

Also tracked (weighted 1x): trustworthiness/safety, collaborative (multi-robot control),
controlled/steerable generation of videos or actions, and other features (e.g. async
inference, streaming, on-device).

## Scoring guidance

- Score each metric 0–10 from evidence in the paper; use **"N/A"** when the paper does not
  address a metric — do not guess or penalize with a 0.
- Be **skeptical of self-reported numbers**. Note the dataset a model was trained/finetuned
  on; the same model name on a different dataset is a different system.
- Reward reproducibility (released code/data/weights) under `impact`.
