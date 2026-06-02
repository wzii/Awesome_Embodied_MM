"""Papers with Code enrichment — has-code / repo link signal.

Best-effort lookup by arXiv id. This is one HTTP call per paper, so callers should pass only
the shortlist (e.g. post-filter core/adjacent papers) and respect ``max_lookups``.
"""

from __future__ import annotations

import time

import requests

from wam.config import Config
from wam.logging import get_logger
from wam.models import PaperRecord

log = get_logger("source.pwc")

API = "https://paperswithcode.com/api/v1/papers/"


def _repo_for_arxiv(aid: str, timeout: int) -> str | None:
    try:
        r = requests.get(API, params={"arxiv_id": aid}, timeout=timeout)
        r.raise_for_status()
        results = r.json().get("results") or []
        if not results:
            return None
        pid = results[0]["id"]
        rr = requests.get(f"{API}{pid}/repositories/", timeout=timeout)
        rr.raise_for_status()
        repos = rr.json().get("results") or []
        if not repos:
            return None
        # Prefer the official repo if flagged, else the most-starred.
        repos.sort(key=lambda x: (x.get("is_official", False), x.get("stars", 0)), reverse=True)
        return repos[0].get("url")
    except Exception as e:  # noqa: BLE001
        log.debug("pwc lookup failed for %s: %s", aid, e)
        return None


def enrich(cfg: Config, records: list[PaperRecord], *, max_lookups: int = 60) -> list[PaperRecord]:
    if not (cfg.get("sources.papers_with_code", {}) or {}).get("enabled", True):
        return records
    timeout = cfg.get("constants.request_timeout", 90)
    found = 0
    for rec in records[:max_lookups]:
        if not rec.arxiv_id or rec.links.code:
            continue
        url = _repo_for_arxiv(rec.arxiv_id, timeout)
        if url:
            rec.links.code = url
            rec.has_code = True
            found += 1
        time.sleep(0.5)
    log.info("pwc found code for %d papers", found)
    return records
