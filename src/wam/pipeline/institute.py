"""Institute stage — extract author affiliations (institutions) per paper (cheap tier).

The author/affiliation block lives on the PDF first page (arXiv metadata rarely carries it),
so we read the cached/downloaded first page and have the cheap model list the distinct
institutions. They're stored RAW on the paper; "top lab" matching against the configured
watch-list happens at render/email time (see ``wam.store.institutes``) so the list can change
without re-extracting. Idempotent + resumable via ``institutes_extracted``.
"""

from __future__ import annotations

import json
import sqlite3
from concurrent.futures import ThreadPoolExecutor, as_completed

from wam.config import Config
from wam.llm import LLMClient
from wam.logging import get_logger
from wam.pipeline.schemas import InstituteResult
from wam.sources import pdf
from wam.store import papers as ps

log = get_logger("pipeline.institute")

SYSTEM = (
    "From the author/affiliation block on this paper's first page, list the DISTINCT research "
    "institutions or companies the authors are affiliated with. Rules:\n"
    "- Use the full canonical name (e.g. 'Google DeepMind', 'Stanford University', 'Tsinghua "
    "University', 'NVIDIA') — not an abbreviation, and not a lab/department name alone.\n"
    "- Only institutions ACTUALLY stated in the text — never guess from the topic or authors.\n"
    "- Deduplicate. Return an empty list if no affiliation is stated.")


def _one(cfg: Config, client: LLMClient, row) -> tuple[str, object | None]:
    """Worker: read PDF first page + list affiliations. Returns (paper_id, InstituteResult|None)."""
    links = json.loads(row["links_json"] or "{}")
    text = pdf.get_text(cfg, row["id"], links.get("pdf") or "", max_chars=3000)
    if not text:
        # Nothing readable (e.g. unreachable PDF) — mark done with no institutes, don't retry.
        return row["id"], InstituteResult(institutes=[])
    user = f"Title: {row['title']}\n\nFirst page (author/affiliation block):\n{text}"
    try:
        res = client.complete_json("institute", SYSTEM, user, InstituteResult,
                                   label="institute", max_tokens=800)
        return row["id"], res
    except Exception as e:  # noqa: BLE001
        log.warning("institute extract failed for %s: %s", row["id"], e)
        return row["id"], None


def run(cfg: Config, client: LLMClient, conn: sqlite3.Connection,
        limit: int | None = None) -> int:
    if not bool(cfg.get("institutes.enabled", True)):
        log.info("institutes disabled in config; skipping")
        return 0
    cap = limit or int(cfg.get("constants.analyze_cap", 40))
    todo = ps.needs_institute(conn, limit=cap)
    workers = int(cfg.get("constants.extract_workers", 6))
    log.info("extracting institutes for %d papers (%d workers)", len(todo), workers)
    done = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(_one, cfg, client, r): r["id"] for r in todo}
        for fut in as_completed(futs):
            pid, res = fut.result()
            if res is not None:
                ps.set_institutes(conn, pid, json.dumps(res.institutes))
            # else: leave institutes_extracted=0 so a transient failure retries next run
            conn.commit()
            done += 1
            if done % 20 == 0:
                log.info("institute progress: %d/%d", done, len(todo))
    log.info("extracted institutes from %d papers", done)
    return done
