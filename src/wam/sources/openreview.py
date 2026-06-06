"""OpenReview source — venue / peer-review signal (api2 search).

Searches OpenReview's note index for our keyword net, restricted to **forum-level** notes
(the actual submissions, not the reviews/comments under them) via ``source=forum``. This
surfaces work at top venues (CoRL, ICLR, NeurIPS, …) — often before/independent of arXiv —
and captures the venue + acceptance status (e.g. "ICLR 2026 Poster" vs "Submitted to ICLR
2026"). Recall-oriented; the LLM filter makes the final core/adjacent/drop call. Each source
failure degrades gracefully (returns what it has) rather than crashing the run.
"""

from __future__ import annotations

import time
from datetime import date, datetime, timedelta

import requests

from wam.config import Config
from wam.logging import get_logger
from wam.models import Links, PaperRecord

log = get_logger("source.openreview")

API = "https://api2.openreview.net/notes/search"


def _cv(content: dict, key: str):
    """OpenReview v2 wraps each content field as {"value": ...}; unwrap it."""
    v = content.get(key)
    return v.get("value") if isinstance(v, dict) else v


def fetch(cfg: Config, *, lookback_days: int | None = None) -> list[PaperRecord]:
    scfg = cfg.get("sources.openreview", {}) or {}
    if not scfg.get("enabled", True):
        return []
    keywords = (cfg.get("keywords.core", []) or []) + (cfg.get("keywords.adjacent", []) or [])
    per_term = int(scfg.get("per_term", 30))
    lookback_days = lookback_days or cfg.get("constants.lookback_days", 60)
    cutoff = date.today() - timedelta(days=lookback_days)
    timeout = cfg.get("constants.request_timeout", 90)
    headers = {"User-Agent": "Awesome-Embodied-MM/0.1 (research digest)"}

    out: dict[str, PaperRecord] = {}
    for kw in keywords:
        try:
            resp = requests.get(API, params={"term": kw, "source": "forum", "limit": per_term},
                                timeout=timeout, headers=headers)
            if resp.status_code != 200:
                log.warning("openreview %s for term %r", resp.status_code, kw)
                continue
            notes = resp.json().get("notes", []) or []
        except (requests.RequestException, ValueError) as e:
            log.warning("openreview request error for %r: %s", kw, e)
            continue
        for n in notes:
            nid = n.get("id")
            if not nid or nid in out:
                continue
            c = n.get("content", {}) or {}
            title = _cv(c, "title")
            if not title:
                continue
            cdate = n.get("pdate") or n.get("cdate")
            published = None
            if cdate:
                try:
                    published = datetime.utcfromtimestamp(cdate / 1000).date()
                except (OSError, OverflowError, ValueError):
                    published = None
            if published and published < cutoff:
                continue
            venue = _cv(c, "venue") or ""
            abstract = _cv(c, "abstract")
            authors = _cv(c, "authors")
            out[nid] = PaperRecord(
                id=f"openreview:{nid}",
                source="openreview",
                title=" ".join(title.split()),
                authors=authors if isinstance(authors, list) else [],
                published=published.isoformat() if published else None,
                abstract=" ".join(abstract.split()) if abstract else None,
                categories=[t for t in ("OpenReview", venue) if t],
                links=Links(abs=f"https://openreview.net/forum?id={nid}",
                            pdf=f"https://openreview.net/pdf?id={nid}"),
            )
        time.sleep(1)  # be polite to OpenReview
    recs = list(out.values())
    log.info("openreview returned %d unique candidates within lookback", len(recs))
    return recs
