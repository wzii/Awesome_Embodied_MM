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

ALL_STAGES = ["fetch", "filter", "summarize", "analyze", "extract", "score", "innovation",
              "links", "people", "trends", "render", "email"]
LLM_STAGES = {"filter", "summarize", "analyze", "extract", "score", "innovation", "people",
              "trends"}


def main() -> int:
    ap = argparse.ArgumentParser(description="Awesome-WAM local pipeline runner")
    ap.add_argument("--stages", default=",".join(ALL_STAGES),
                    help=f"comma list from: {','.join(ALL_STAGES)}")
    ap.add_argument("--fetch-only", action="store_true")
    ap.add_argument("--limit", type=int, default=None,
                    help="cap papers per LLM stage (for quick verification)")
    ap.add_argument("--debug", action="store_true")
    ap.add_argument("--email-test", metavar="ADDR",
                    help="send the digest only to ADDR (test) instead of SUBSCRIBERS")
    args = ap.parse_args()

    stages = ["fetch"] if args.fetch_only else [s.strip() for s in args.stages.split(",") if s.strip()]
    cfg = load_config()
    setup_logging(level=cfg.get("logging.level", "INFO"),
                  log_dir=cfg.get("logging.log_dir", "logs"), debug=args.debug or None)
    log = get_logger("run")
    log.info("stages: %s", stages)

    # LLM client only needed for the stages that call models.
    client = None
    if any(s in LLM_STAGES for s in stages):
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
            elif stage == "extract":
                from wam.pipeline import extract
                n = extract.run(cfg, client, db.conn, limit=args.limit)
                db.log_run("extract", n, n, COST.cost_usd)
            elif stage == "score":
                from wam.pipeline import score
                n = score.run(cfg, client, db.conn, limit=args.limit)
                db.log_run("score", n, n, COST.cost_usd)
            elif stage == "innovation":
                from wam.pipeline import innovation
                n = innovation.run(cfg, client, db.conn, limit=args.limit)
                db.log_run("innovation", n, n, COST.cost_usd)
            elif stage == "links":
                from wam.pipeline import links
                n = links.run(cfg, db.conn, limit=args.limit)
                db.log_run("links", 0, n)
            elif stage == "people":
                from wam.pipeline import people
                c = people.run(cfg, client, db.conn, limit=args.limit)
                db.log_run("people", c["authors"], c["groups"], COST.cost_usd, notes=str(c))
            elif stage == "trends":
                from wam.pipeline import trends
                n = trends.run(cfg, client, db.conn)
                db.log_run("trends", 0, n, COST.cost_usd)
            elif stage == "render":
                from wam.render import readme as rnd
                rnd.render_readme(cfg, db.conn)
                rnd.render_digest(cfg, db.conn)
                rnd.export_benchmarks_csv(cfg, db.conn)
                issues = rnd.link_integrity(db.conn)
                if issues:
                    log.warning("link integrity: %d issues (e.g. %s)", len(issues), issues[:3])
                db.log_run("render", 0, 0, notes=f"{len(issues)} link issues")
            elif stage == "email":
                from wam.notify import mailer
                n = mailer.send(cfg, db.conn, test_to=args.email_test)
                db.log_run("email", 0, n)
            else:
                log.warning("unknown stage: %s", stage)

    log.info(COST.summary())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
