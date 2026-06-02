"""Configuration loading.

Loads ``config/config.yaml`` plus the human-readable ``config/profile.md`` and resolves
the project root. Environment variables (e.g. API keys) are loaded from a local ``.env``
when present so dev runs work without exporting anything.
"""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

try:  # optional: only needed for local dev convenience
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover
    load_dotenv = None


def project_root() -> Path:
    """Repo root = two levels up from this file (src/wam/config.py)."""
    return Path(__file__).resolve().parents[2]


class Config:
    """Thin wrapper over the parsed config dict with dotted-path access."""

    def __init__(self, data: dict[str, Any], root: Path):
        self._data = data
        self.root = root

    def get(self, path: str, default: Any = None) -> Any:
        """Fetch a nested value by dotted path, e.g. ``config.get("models.tiers.cheap")``."""
        node: Any = self._data
        for part in path.split("."):
            if not isinstance(node, dict) or part not in node:
                return default
            node = node[part]
        return node

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    @property
    def data(self) -> dict[str, Any]:
        return self._data

    # --- convenience resolvers -------------------------------------------------
    def path(self, key: str) -> Path:
        """Resolve a configured relative path (under ``paths.*``) against the repo root."""
        rel = self.get(f"paths.{key}")
        if rel is None:
            raise KeyError(f"paths.{key} not configured")
        return (self.root / rel).resolve()

    def require_env(self, env_var: str) -> str:
        val = os.environ.get(env_var)
        if not val:
            raise RuntimeError(f"Required environment variable {env_var} is not set")
        return val

    def profile_text(self) -> str:
        """The research-interest profile fed to relevance/scoring prompts."""
        return (self.root / "config" / "profile.md").read_text(encoding="utf-8")

    def model_for_stage(self, stage: str, fallback_tier: str = "mid") -> str:
        """Resolve the OpenRouter model id for a pipeline stage via stage_tiers -> tiers."""
        tier = self.get(f"models.stage_tiers.{stage}", fallback_tier)
        model = self.get(f"models.tiers.{tier}")
        if not model:
            raise KeyError(f"No model configured for tier '{tier}'")
        return model


@lru_cache(maxsize=1)
def load_config(config_path: str | None = None) -> Config:
    """Load and cache the project config. Also loads ``.env`` if available."""
    root = project_root()
    if load_dotenv is not None:
        load_dotenv(root / ".env")
    path = Path(config_path) if config_path else root / "config" / "config.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return Config(data, root)
