"""Central logging.

A single console handler at the configured level; in **debug mode** an additional file
sink captures *everything* for the run under ``logs/run-<date>.log`` (gitignored). The LLM
client logs a structured record per call (tier, model, tokens, cost, latency) so a debug
run is a full, replayable trace. A module-level :class:`CostTracker` accumulates spend and
emits a per-run summary.
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from datetime import date
from logging.handlers import RotatingFileHandler
from pathlib import Path

_CONFIGURED = False
_FMT = "%(asctime)s %(levelname)-7s %(name)s | %(message)s"


def is_debug() -> bool:
    return os.environ.get("WAM_DEBUG", "").lower() in {"1", "true", "yes"}


def setup_logging(level: str = "INFO", log_dir: str | Path = "logs", debug: bool | None = None,
                  run_date: str | None = None) -> logging.Logger:
    """Configure root logging once. Returns the ``wam`` logger.

    When ``debug`` (or ``WAM_DEBUG`` env) is set, attaches a rotating file handler at DEBUG
    level writing the full run trace to ``<log_dir>/run-<date>.log``.
    """
    global _CONFIGURED
    debug = is_debug() if debug is None else debug
    root = logging.getLogger()
    base_level = logging.DEBUG if debug else getattr(logging, level.upper(), logging.INFO)
    root.setLevel(logging.DEBUG if debug else base_level)

    if not _CONFIGURED:
        console = logging.StreamHandler()
        console.setLevel(base_level)
        console.setFormatter(logging.Formatter(_FMT))
        root.addHandler(console)

        if debug:
            d = Path(log_dir)
            d.mkdir(parents=True, exist_ok=True)
            stamp = run_date or date.today().isoformat()
            fh = RotatingFileHandler(d / f"run-{stamp}.log", maxBytes=20_000_000,
                                     backupCount=5, encoding="utf-8")
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(logging.Formatter(_FMT))
            root.addHandler(fh)
        _CONFIGURED = True

    return logging.getLogger("wam")


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(f"wam.{name}")


@dataclass
class CostTracker:
    """Accumulates token usage + estimated cost across a run."""

    calls: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0
    by_model: dict[str, dict[str, float]] = field(default_factory=dict)

    def record(self, model: str, in_tok: int, out_tok: int, cost: float) -> None:
        self.calls += 1
        self.input_tokens += in_tok
        self.output_tokens += out_tok
        self.cost_usd += cost
        m = self.by_model.setdefault(model, {"calls": 0, "in": 0, "out": 0, "cost": 0.0})
        m["calls"] += 1
        m["in"] += in_tok
        m["out"] += out_tok
        m["cost"] += cost

    def summary(self) -> str:
        parts = [f"{self.calls} calls", f"{self.input_tokens}+{self.output_tokens} tok",
                 f"${self.cost_usd:.4f}"]
        per = ", ".join(f"{k}: ${v['cost']:.4f}" for k, v in sorted(self.by_model.items()))
        return f"LLM usage: {' / '.join(parts)}" + (f" [{per}]" if per else "")


# One shared tracker per process; the LLM client writes to it.
COST = CostTracker()
