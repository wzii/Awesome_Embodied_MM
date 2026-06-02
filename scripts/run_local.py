#!/usr/bin/env python3
"""Local pipeline runner (dev/verify).

Phase 2 supports the fetch+dedup stage. Later phases extend this with --filter, --analyze,
--score, --render, etc. Examples:

    python scripts/run_local.py --fetch-only
    WAM_DEBUG=1 python scripts/run_local.py --fetch-only   # full trace to logs/
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from wam.config import load_config  # noqa: E402
from wam.logging import COST, get_logger, setup_logging  # noqa: E402
from wam.pipeline import fetch as fetch_stage  # noqa: E402
from wam.store import Database  # noqa: E402
from wam.store import papers as paper_store  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description="Awesome-WAM local pipeline runner")
    ap.add_argument("--fetch-only", action="store_true", help="run only fetch + dedup")
    ap.add_argument("--debug", action="store_true", help="enable full debug logging")
    args = ap.parse_args()

    cfg = load_config()
    setup_logging(level=cfg.get("logging.level", "INFO"),
                  log_dir=cfg.get("logging.log_dir", "logs"), debug=args.debug or None)
    log = get_logger("run")

    with Database(cfg) as db:
        before = paper_store.count(db.conn)
        new = fetch_stage.run(cfg, db.conn)
        after = paper_store.count(db.conn)
        db.log_run("fetch", n_in=after, n_out=len(new),
                   cost_usd=COST.cost_usd, notes=f"{before}->{after} papers")
        log.info("fetch complete: %d new (db now %d papers)", len(new), after)
        for r in new[:10]:
            log.info("  + [%s] %s", r.source, r.title[:90])

    if not args.fetch_only:
        log.warning("only --fetch-only is implemented so far (Phase 2); later phases add more")
    log.info(COST.summary())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
