"""arXiv source — the core candidate feed.

Queries the arXiv Atom API for recent papers in the configured categories matching a broad
keyword net (WAM + adjacent fields). The LLM filter makes the final core/adjacent/drop call
later; here we just cast a wide, recall-oriented net within the lookback window.
"""

from __future__ import annotations

import time
from datetime import date, datetime, timedelta

import feedparser
import requests

from wam.config import Config
from wam.logging import get_logger
from wam.models import Links, PaperRecord

log = get_logger("source.arxiv")

API = "http://export.arxiv.org/api/query"


def _build_query(categories: list[str], keywords: list[str]) -> str:
    cats = " OR ".join(f"cat:{c}" for c in categories)
    kws = " OR ".join(f'all:"{k}"' for k in keywords)
    return f"({cats}) AND ({kws})"


def _arxiv_id(entry) -> str:
    # entry.id like http://arxiv.org/abs/2506.01234v2 -> 2506.01234
    raw = entry.id.rsplit("/abs/", 1)[-1]
    return raw.split("v")[0] if "v" in raw else raw


def fetch(cfg: Config, *, max_results: int | None = None,
          lookback_days: int | None = None) -> list[PaperRecord]:
    scfg = cfg.get("sources.arxiv", {}) or {}
    if not scfg.get("enabled", True):
        return []
    categories = scfg.get("categories", ["cs.RO", "cs.AI", "cs.LG", "cs.CV"])
    keywords = (cfg.get("keywords.core", []) or []) + (cfg.get("keywords.adjacent", []) or [])
    max_results = max_results or scfg.get("max_results", 300)
    lookback_days = lookback_days or cfg.get("constants.lookback_days", 60)
    cutoff = date.today() - timedelta(days=lookback_days)

    params = {
        "search_query": _build_query(categories, keywords),
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    log.info("arxiv query: %s (max=%d, since=%s)", params["search_query"], max_results, cutoff)
    resp = requests.get(API, params=params, timeout=cfg.get("constants.request_timeout", 90))
    resp.raise_for_status()
    feed = feedparser.parse(resp.text)

    records: list[PaperRecord] = []
    for e in feed.entries:
        try:
            published = datetime(*e.published_parsed[:6]).date()
        except Exception:  # noqa: BLE001
            published = None
        if published and published < cutoff:
            continue
        aid = _arxiv_id(e)
        pdf = next((l.href for l in getattr(e, "links", []) if l.get("type") == "application/pdf"),
                   f"https://arxiv.org/pdf/{aid}")
        records.append(PaperRecord(
            id=f"arxiv:{aid}",
            source="arxiv",
            title=" ".join(e.title.split()),
            authors=[a.name for a in getattr(e, "authors", [])],
            published=published.isoformat() if published else None,
            abstract=" ".join(e.summary.split()) if hasattr(e, "summary") else None,
            categories=[t.term for t in getattr(e, "tags", [])],
            links=Links(abs=f"https://arxiv.org/abs/{aid}", pdf=pdf),
        ))
    log.info("arxiv returned %d entries, %d within lookback", len(feed.entries), len(records))
    time.sleep(3)  # be polite to arXiv
    return records
