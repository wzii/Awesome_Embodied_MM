#!/usr/bin/env python3
"""Local pipeline runner (dev/verify).

Runs any subset of pipeline stages against the SQLite store. Stages are idempotent and
resumable (each only processes rows that still need it), so re-running is cheap.

    python scripts/run_local.py --stages fetch
    python scripts/run_local.py --stages filter,summarize,analyze,score,innovation
    WAM_DEBUG=1 python scripts/run_local.py            # full pipeline, full trace
    python scripts/run_local.py --fetch-only
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from wam.config import load_config  # noqa: E402
from wam.logging import COST, get_logger, setup_logging  # noqa: E402
from wam.store import Database  # noqa: E402
from wam.store import papers as ps  # noqa: E402

ALL_STAGES = ["fetch", "filter", "summarize", "analyze", "score", "innovation"]


def main() -> int:
    ap = argparse.ArgumentParser(description="Awesome-WAM local pipeline runner")
    ap.add_argument("--stages", default=",".join(ALL_STAGES),
                    help=f"comma list from: {','.join(ALL_STAGES)}")
    ap.add_argument("--fetch-only", action="store_true")
    ap.add_argument("--limit", type=int, default=None,
                    help="cap papers per LLM stage (for quick verification)")
    ap.add_argument("--debug", action="store_true")
    args = ap.parse_args()

    stages = ["fetch"] if args.fetch_only else [s.strip() for s in args.stages.split(",") if s.strip()]
    cfg = load_config()
    setup_logging(level=cfg.get("logging.level", "INFO"),
                  log_dir=cfg.get("logging.log_dir", "logs"), debug=args.debug or None)
    log = get_logger("run")
    log.info("stages: %s", stages)

    # LLM client only needed for non-fetch stages.
    client = None
    if any(s != "fetch" for s in stages):
        from wam.llm import LLMClient
        client = LLMClient(cfg)

    with Database(cfg) as db:
        for stage in stages:
            if stage == "fetch":
                from wam.pipeline import fetch
                new = fetch.run(cfg, db.conn)
                db.log_run("fetch", ps.count(db.conn), len(new), COST.cost_usd)
            elif stage == "filter":
                from wam.pipeline import filter as filt
                c = filt.run(cfg, client, db.conn, limit=args.limit)
                db.log_run("filter", sum(c.values()), c.get("core", 0) + c.get("adjacent", 0),
                           COST.cost_usd, notes=str(c))
            elif stage == "summarize":
                from wam.pipeline import summarize
                n = summarize.run(cfg, client, db.conn, limit=args.limit)
                db.log_run("summarize", n, n, COST.cost_usd)
            elif stage == "analyze":
                from wam.pipeline import analyze
                n = analyze.run(cfg, client, db.conn, limit=args.limit)
                db.log_run("analyze", n, n, COST.cost_usd)
            elif stage == "score":
                from wam.pipeline import score
                n = score.run(cfg, client, db.conn, limit=args.limit)
                db.log_run("score", n, n, COST.cost_usd)
            elif stage == "innovation":
                from wam.pipeline import innovation
                n = innovation.run(cfg, client, db.conn, limit=args.limit)
                db.log_run("innovation", n, n, COST.cost_usd)
            else:
                log.warning("unknown stage: %s", stage)

    log.info(COST.summary())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
