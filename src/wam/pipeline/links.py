"""Links enrichment — find each paper's GitHub / Hugging Face repo.

Repo URLs are almost always in the PDF body ("Code is available at https://github.com/…"),
not the abstract — so we scan the (cached) full text. A keyword-proximity heuristic picks the
authors' own repo over baselines/comparisons. Found URLs are written into ``links_json`` as
``code`` (GitHub) and ``hf`` (Hugging Face); the README and email then surface them.
"""

from __future__ import annotations

import json
import re
import sqlite3

from wam.config import Config
from wam.logging import get_logger
from wam.sources import papers_with_code, pdf

log = get_logger("pipeline.links")

_GH = re.compile(r"https?://github\.com/[A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+")
_HF = re.compile(r"https?://huggingface\.co/[A-Za-z0-9_.\-/]+")
# repos that are almost always dependencies/baselines, not the paper's own.
_GH_DENY = ("github.com/huggingface", "github.com/pytorch", "github.com/openai",
            "github.com/google", "github.com/facebookresearch/detectron")
_KEYWORDS = ("code", "project", "available", "github", "hugging", "weights", "released",
             "release", "repo", "page", "checkpoint")


def _clean(url: str) -> str:
    return url.rstrip(").,;:'\"]}").rstrip("/")


def _prep(text: str) -> str:
    """Rejoin URLs broken across PDF lines: drop hyphenated breaks, unwrap newlines."""
    return text.replace("-\n", "").replace("\n", " ")


def _best(text: str, pattern: re.Pattern, deny: tuple = ()) -> str | None:
    cands = [(m.start(), _clean(m.group(0))) for m in pattern.finditer(text)]
    cands = [(p, u) for p, u in cands if not any(d in u.lower() for d in deny)]
    if not cands:
        return None
    low = text.lower()
    for pos, url in cands:  # prefer a URL sitting right after a "code/project/…" cue
        if any(k in low[max(0, pos - 60):pos] for k in _KEYWORDS):
            return url
    return cands[0][1]


def run(cfg: Config, conn: sqlite3.Connection, limit: int | None = None,
        download: bool = True, use_pwc: bool = True) -> int:
    q = ("SELECT id, abstract, links_json FROM papers WHERE track IN ('core','adjacent')")
    if limit:
        q += f" LIMIT {int(limit)}"
    rows = conn.execute(q).fetchall()
    log.info("links: scanning %d papers (download=%s, pwc=%s)", len(rows), download, use_pwc)
    found = 0
    for i, r in enumerate(rows):
        links = json.loads(r["links_json"] or "{}")
        if links.get("code") and links.get("hf"):
            continue
        pdf_url = links.get("pdf") or (f"https://arxiv.org/pdf/{r['id'].split(':',1)[1]}"
                                       if r["id"].startswith("arxiv:") else "")
        text = pdf.get_text(cfg, r["id"], pdf_url if download else "", max_chars=80000)
        blob = _prep((text or "") + "\n" + (r["abstract"] or ""))  # rejoin line-broken URLs
        changed = False
        if blob.strip():
            if not links.get("code"):
                gh = _best(blob, _GH, _GH_DENY)
                if gh:
                    links["code"], changed = gh, True
            if not links.get("hf"):
                hf = _best(blob, _HF)
                if hf:
                    links["hf"], changed = hf, True
        # Fallback: Papers-with-Code (canonical arXiv->repo) when still no code link.
        if use_pwc and not links.get("code") and r["id"].startswith("arxiv:"):
            url = papers_with_code._repo_for_arxiv(r["id"].split(":", 1)[1],
                                                   cfg.get("constants.request_timeout", 90))
            if url:
                links["code"], changed = _clean(url), True
        if changed:
            conn.execute("UPDATE papers SET links_json=? WHERE id=?",
                         (json.dumps(links), r["id"]))
            found += 1
        if i and i % 25 == 0:
            conn.commit()
            log.info("links progress: %d/%d (found %d)", i, len(rows), found)
    conn.commit()
    log.info("links: enriched %d papers with code/HF", found)
    return found
