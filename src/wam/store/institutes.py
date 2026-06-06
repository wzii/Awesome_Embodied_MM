"""Top-institute matching.

Per-paper author affiliations are extracted by the ``institute`` stage and stored raw on the
paper (``institutes_json``). The *watch-list* of top labs/teams/institutes lives in config
(``institutes.top``, alias-aware), so it can change without re-extracting. Matching is
case-insensitive substring of any alias within any of the paper's affiliations.
"""

from __future__ import annotations

import json

from wam.config import Config


def top_entries(cfg: Config) -> list[dict]:
    out = []
    for e in cfg.get("institutes.top", []) or []:
        if isinstance(e, dict) and e.get("name"):
            out.append({"name": e["name"], "aliases": e.get("aliases", []) or []})
        elif isinstance(e, str):
            out.append({"name": e, "aliases": []})
    return out


def match_top(institutes: list[str] | None, cfg: Config) -> list[str]:
    """Canonical names of configured top institutes the paper's affiliations match."""
    if not institutes:
        return []
    hay = " ; ".join(institutes).lower()
    matched: list[str] = []
    for e in top_entries(cfg):
        cands = [e["name"], *e["aliases"]]
        if any(c and c.lower() in hay for c in cands):
            matched.append(e["name"])
    return matched


def paper_institutes(institutes_json: str | None) -> list[str]:
    """Decode a paper's stored ``institutes_json`` into a list (safe)."""
    try:
        v = json.loads(institutes_json or "[]")
        return [str(x) for x in v] if isinstance(v, list) else []
    except Exception:  # noqa: BLE001
        return []
