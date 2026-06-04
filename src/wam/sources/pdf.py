"""PDF text extraction with on-disk caching.

Benchmark numbers live in the paper body (tables), not the abstract, so the extractor needs
full text. We download each PDF once, extract text with PyMuPDF, and cache it keyed by a
content hash so arXiv revisions are re-extracted but repeats are free.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import requests

from wam.config import Config
from wam.logging import get_logger

log = get_logger("source.pdf")


def _cache_dir(cfg: Config) -> Path:
    d = cfg.path("pdf_cache")
    d.mkdir(parents=True, exist_ok=True)
    return d


def get_text(cfg: Config, paper_id: str, pdf_url: str, *, max_chars: int = 60000) -> str | None:
    """Return cached/extracted text for a paper (truncated to max_chars), or None on failure."""
    safe = paper_id.replace("/", "_").replace(":", "_")
    cache = _cache_dir(cfg) / f"{safe}.txt"
    if cache.exists():
        return cache.read_text(encoding="utf-8")[:max_chars]
    if not pdf_url:
        return None
    try:
        import fitz  # PyMuPDF
    except ImportError:  # pragma: no cover
        log.warning("PyMuPDF not installed; skipping PDF extraction")
        return None
    try:
        resp = requests.get(pdf_url, timeout=cfg.get("constants.request_timeout", 90),
                            headers={"User-Agent": "Awesome-Embodied-MM/0.1"})
        resp.raise_for_status()
        with fitz.open(stream=resp.content, filetype="pdf") as doc:
            text = "\n".join(page.get_text() for page in doc)
    except Exception as e:  # noqa: BLE001
        log.warning("PDF extraction failed for %s: %s", paper_id, e)
        return None
    cache.write_text(text, encoding="utf-8")
    h = hashlib.sha256(resp.content).hexdigest()
    cache.with_suffix(".hash").write_text(h, encoding="utf-8")
    log.debug("cached PDF text for %s (%d chars)", paper_id, len(text))
    return text[:max_chars]
