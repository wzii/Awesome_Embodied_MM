"""Embodied / physical-AI news via RSS.

News items are normalized into ``PaperRecord`` with ``source='news'`` so they flow through
the same store. They get a light summary later but not the full WAM rubric.
"""

from __future__ import annotations

import hashlib
from datetime import date, datetime, timedelta

import feedparser

from wam.config import Config
from wam.logging import get_logger
from wam.models import Links, PaperRecord

log = get_logger("source.news")


def fetch(cfg: Config, *, lookback_days: int | None = None) -> list[PaperRecord]:
    ncfg = cfg.get("sources.news", {}) or {}
    if not ncfg.get("enabled", True):
        return []
    feeds = ncfg.get("feeds", []) or []
    lookback_days = lookback_days or cfg.get("constants.lookback_days", 60)
    cutoff = date.today() - timedelta(days=lookback_days)

    records: list[PaperRecord] = []
    for url in feeds:
        try:
            feed = feedparser.parse(url)
        except Exception as e:  # noqa: BLE001
            log.warning("news feed failed %s: %s", url, e)
            continue
        outlet = feed.feed.get("title", url) if hasattr(feed, "feed") else url
        for e in feed.entries:
            try:
                published = datetime(*e.published_parsed[:6]).date()
            except Exception:  # noqa: BLE001
                published = None
            if published and published < cutoff:
                continue
            link = getattr(e, "link", "")
            uid = hashlib.sha1(link.encode("utf-8")).hexdigest()[:16]
            summary = getattr(e, "summary", "") or ""
            records.append(PaperRecord(
                id=f"news:{uid}",
                source="news",
                title=" ".join(getattr(e, "title", "(untitled)").split()),
                authors=[outlet],
                published=published.isoformat() if published else None,
                abstract=" ".join(summary.split())[:2000],
                categories=["news"],
                links=Links(abs=link),
            ))
    log.info("news: %d items within lookback from %d feeds", len(records), len(feeds))
    return records
