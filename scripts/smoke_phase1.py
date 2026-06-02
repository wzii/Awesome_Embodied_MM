#!/usr/bin/env python3
"""Phase 1 smoke test: config, logging, DB init, and (if a key is set) each LLM tier.

Usage:
    python scripts/smoke_phase1.py            # config + logging + DB; LLM only if key present
    WAM_DEBUG=1 python scripts/smoke_phase1.py --llm   # force LLM tier calls, full debug log

Verifies the Phase 1 foundation without needing the rest of the pipeline.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# Allow running from a checkout without installing the package.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pydantic import BaseModel, Field  # noqa: E402

from wam.config import load_config  # noqa: E402
from wam.logging import COST, get_logger, setup_logging  # noqa: E402
from wam.store import Database  # noqa: E402


class Ping(BaseModel):
    ok: bool = Field(description="always true")
    tier: str = Field(description="the tier name you were told to echo")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--llm", action="store_true", help="force LLM tier calls (needs key)")
    args = ap.parse_args()

    cfg = load_config()
    setup_logging(level=cfg.get("logging.level", "INFO"),
                  log_dir=cfg.get("logging.log_dir", "logs"))
    log = get_logger("smoke")

    log.info("project root: %s", cfg.root)
    log.info("tiers: %s", cfg.get("models.tiers"))

    # DB init
    with Database(cfg) as db:
        n = db.conn.execute("SELECT count(*) AS c FROM papers").fetchone()["c"]
        log.info("db ok at %s (papers rows=%d)", db.path, n)
        db.log_run("smoke", n_in=0, n_out=0, notes="phase1 smoke")

    key = os.environ.get(cfg.get("provider.api_key_env", "OPENROUTER_API_KEY"))
    if not (args.llm or key):
        log.info("no %s set and --llm not passed; skipping LLM calls. Foundation OK.",
                 cfg.get("provider.api_key_env"))
        return 0
    if not key:
        log.error("--llm requested but %s is not set", cfg.get("provider.api_key_env"))
        return 2

    from wam.llm import LLMClient  # imported late so missing key doesn't block the rest
    client = LLMClient(cfg)
    for tier in ("cheap", "mid", "strong"):
        try:
            out = client.complete_json(
                tier,
                system="You are a connectivity check.",
                user=f"Echo back that you are reachable on the '{tier}' tier.",
                schema=Ping, label=f"ping-{tier}", max_tokens=200,
            )
            log.info("tier %-6s -> %s (model=%s)", tier, out.model_dump(),
                     client.resolve_model(tier))
        except Exception as e:  # noqa: BLE001
            log.error("tier %s FAILED: %s", tier, e)

    log.info(COST.summary())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
