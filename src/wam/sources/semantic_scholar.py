"""Semantic Scholar enrichment.

Adds citation signals (total + influential) and a DOI/open-access PDF link to existing
records, keyed by arXiv id via the batch endpoint. Best-effort: failures leave records as-is.
"""

from __future__ import annotations

import os
import time

import requests

from wam.config import Config
from wam.logging import get_logger
from wam.models import PaperRecord

log = get_logger("source.s2")

BATCH = "https://api.semanticscholar.org/graph/v1/paper/batch"
FIELDS = "citationCount,influentialCitationCount,externalIds,openAccessPdf"


def enrich(cfg: Config, records: list[PaperRecord]) -> list[PaperRecord]:
    scfg = cfg.get("sources.semantic_scholar", {}) or {}
    if not scfg.get("enabled", True):
        return records
    arxiv_recs = [r for r in records if r.arxiv_id]
    if not arxiv_recs:
        return records
    by_aid = {r.arxiv_id: r for r in arxiv_recs}
    ids = [f"ARXIV:{aid}" for aid in by_aid]

    headers = {}
    key = os.environ.get(scfg.get("api_key_env", "SEMANTIC_SCHOLAR_API_KEY") or "")
    if key:
        headers["x-api-key"] = key

    enriched = 0
    for chunk_start in range(0, len(ids), 500):  # batch endpoint caps at 500 ids
        chunk = ids[chunk_start:chunk_start + 500]
        try:
            resp = requests.post(BATCH, params={"fields": FIELDS}, json={"ids": chunk},
                                 headers=headers, timeout=cfg.get("constants.request_timeout", 90))
            if resp.status_code == 429:
                log.warning("s2 rate-limited; backing off")
                time.sleep(5)
                resp = requests.post(BATCH, params={"fields": FIELDS}, json={"ids": chunk},
                                     headers=headers, timeout=90)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:  # noqa: BLE001
            log.warning("s2 batch failed: %s", e)
            continue
        for s2_id, item in zip(chunk, data):
            if not item:
                continue
            aid = s2_id.split("ARXIV:", 1)[1]
            rec = by_aid.get(aid)
            if not rec:
                continue
            rec.citations = item.get("citationCount") or 0
            rec.influential_citations = item.get("influentialCitationCount") or 0
            ext = item.get("externalIds") or {}
            if ext.get("DOI"):
                rec.links.doi = f"https://doi.org/{ext['DOI']}"
            oa = item.get("openAccessPdf") or {}
            if oa.get("url") and not rec.links.pdf:
                rec.links.pdf = oa["url"]
            enriched += 1
        time.sleep(1)
    log.info("s2 enriched %d/%d records", enriched, len(arxiv_recs))
    return records
