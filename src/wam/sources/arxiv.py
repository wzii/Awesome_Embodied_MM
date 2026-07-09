"""arXiv source — the core candidate feed.

Queries the arXiv Atom API for recent papers in the configured categories matching a broad
keyword net (WAM + adjacent fields). The LLM filter makes the final core/adjacent/drop call
later; here we just cast a wide, recall-oriented net within the lookback window.

Reliability notes: this broad query over a 60-day window *always* matches hundreds of
papers, so a 0-entry response is never legitimate — it means arXiv throttled us (429),
5xx'd, or served a transient empty/half-indexed page. Those silent empty fetches are what
caused whole days with no arXiv papers (the backlog then dumps into a later run). So we
page through results, retry hard with backoff (honouring Retry-After), and treat a
0-entry first page as a *failure* (raising ``ArxivFetchError``) rather than "nothing new".
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

# Must be HTTPS: the http:// endpoint now 301-redirects (and intermittently 503s on the
# redirect), which surfaced as silent empty fetches. Hit https directly.
API = "https://export.arxiv.org/api/query"

# Backoff schedule (seconds before each attempt). Longer than a plain few-second retry:
# GitHub-runner IPs get 429'd in bursts and need real cooling-off, not a token pause.
_BACKOFF = (0, 3, 8, 20, 45, 90)
# Hard ceiling on honoured Retry-After, so a hostile header can't stall the whole run.
_MAX_RETRY_AFTER = 120


class ArxivFetchError(RuntimeError):
    """Raised when the arXiv query cannot be retrieved (throttled / empty / 5xx).

    Distinct from "no new papers": the caller treats this as a fetch *failure* worth
    alerting on, not as a quiet zero-result day.
    """


def _build_query(categories: list[str], keywords: list[str]) -> str:
    cats = " OR ".join(f"cat:{c}" for c in categories)
    kws = " OR ".join(f'all:"{k}"' for k in keywords)
    return f"({cats}) AND ({kws})"


def _arxiv_id(entry) -> str:
    # entry.id like http://arxiv.org/abs/2506.01234v2 -> 2506.01234
    raw = entry.id.rsplit("/abs/", 1)[-1]
    return raw.split("v")[0] if "v" in raw else raw


def _total_results(feed) -> int:
    try:
        return int(feed.feed.get("opensearch_totalresults", 0))
    except (ValueError, TypeError, AttributeError):
        return 0


def _get_page(query: str, start: int, page_size: int, timeout: int, headers: dict,
              *, is_first: bool):
    """Fetch one page with retries. Returns a parsed feed, or None if a non-first page
    is unrecoverable (treated as end-of-results). Raises ArxivFetchError if the *first*
    page can't be retrieved (a real outage/throttle we must not paper over)."""
    params = {
        "search_query": query,
        "start": start,
        "max_results": page_size,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    for attempt, wait in enumerate(_BACKOFF):
        if wait:
            time.sleep(wait)
        try:
            resp = requests.get(API, params=params, timeout=timeout, headers=headers)
            if resp.status_code == 429 or resp.status_code >= 500:
                retry_after = resp.headers.get("Retry-After")
                log.warning("arxiv %s at start=%d (attempt %d/%d)%s", resp.status_code,
                            start, attempt + 1, len(_BACKOFF),
                            f", Retry-After={retry_after}" if retry_after else "")
                if retry_after:
                    try:
                        time.sleep(min(float(retry_after), _MAX_RETRY_AFTER))
                    except (ValueError, TypeError):
                        pass
                continue
            resp.raise_for_status()
            feed = feedparser.parse(resp.text)
            if feed.entries:
                return feed
            # Well-formed but 0 entries. Empty body or a total>0 first page => transient
            # (throttle / half-built index) -> retry. A total==0 first page, or any empty
            # later page, is a genuine end-of-results.
            if not resp.text.strip():
                log.warning("arxiv empty body at start=%d (attempt %d)", start, attempt + 1)
                continue
            if is_first and _total_results(feed) > 0:
                log.warning("arxiv 0 entries but totalResults>0 at start=%d (attempt %d) — "
                            "transient, retrying", start, attempt + 1)
                continue
            return feed
        except requests.RequestException as e:
            log.warning("arxiv request error at start=%d (attempt %d): %s",
                        start, attempt + 1, e)
    if is_first:
        raise ArxivFetchError(
            f"arXiv first-page fetch failed after {len(_BACKOFF)} attempts (throttled/empty)")
    log.error("arxiv page fetch failed at start=%d after retries; returning partial", start)
    return None


def fetch(cfg: Config, *, max_results: int | None = None,
          lookback_days: int | None = None) -> list[PaperRecord]:
    scfg = cfg.get("sources.arxiv", {}) or {}
    if not scfg.get("enabled", True):
        return []
    categories = scfg.get("categories", ["cs.RO", "cs.AI", "cs.LG", "cs.CV"])
    keywords = (cfg.get("keywords.core", []) or []) + (cfg.get("keywords.adjacent", []) or [])
    total_cap = max_results or scfg.get("max_results", 300)
    page_size = min(scfg.get("page_size", 100) or 100, total_cap)
    lookback_days = lookback_days or cfg.get("constants.lookback_days", 60)
    cutoff = date.today() - timedelta(days=lookback_days)
    query = _build_query(categories, keywords)
    timeout = cfg.get("constants.request_timeout", 90)
    headers = {"User-Agent": "Awesome-Embodied-MM/0.1 (research digest)"}

    log.info("arxiv query: %s (cap=%d, page=%d, since=%s)", query, total_cap, page_size, cutoff)

    records: list[PaperRecord] = []
    seen_entries = 0
    start = 0
    reached_cutoff = False
    while start < total_cap and not reached_cutoff:
        n = min(page_size, total_cap - start)
        feed = _get_page(query, start, n, timeout, headers, is_first=(start == 0))
        if feed is None or not feed.entries:
            break
        seen_entries += len(feed.entries)
        for e in feed.entries:
            try:
                published = datetime(*e.published_parsed[:6]).date()
            except Exception:  # noqa: BLE001
                published = None
            # Sorted by submittedDate desc: once we cross the cutoff, everything after is
            # older too — stop paging.
            if published and published < cutoff:
                reached_cutoff = True
                continue
            aid = _arxiv_id(e)
            pdf = next((l.href for l in getattr(e, "links", [])
                        if l.get("type") == "application/pdf"),
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
        if len(feed.entries) < n:
            break  # last page
        start += n
        time.sleep(3)  # be polite between pages

    log.info("arxiv returned %d entries, %d within lookback (paged through start=%d)",
             seen_entries, len(records), start)
    return records
