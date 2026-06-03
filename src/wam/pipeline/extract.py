"""Extract stage — normalized benchmark rows + model cards for core papers (mid tier).

Reads the full PDF text (cached) since benchmark numbers live in tables, not the abstract.
Extraction is deliberately conservative: only numbers actually stated, each tagged with the
model variant (name + training dataset) and whether it's the authors' own claim. Capped at
``constants.analyze_cap`` per run.
"""

from __future__ import annotations

import json
import sqlite3

from wam.config import Config
from wam.llm import LLMClient
from wam.logging import get_logger
from wam.pipeline.schemas import ExtractionResult
from wam.sources import pdf
from wam.store import benchmarks as bm
from wam.store import papers as ps

log = get_logger("pipeline.extract")

SYSTEM = (
    "Extract structured experimental results from this World Action Models paper. Rules:\n"
    "- Only report numbers ACTUALLY stated in the text — never estimate or invent.\n"
    "- Each model/system is identified by (model_name, training_dataset). The SAME name "
    "trained/finetuned on a different dataset is a DIFFERENT variant — always capture the "
    "training/finetune dataset when stated.\n"
    "- For each result give the benchmark, task, metric name+value, and any inference "
    "speed/cost with their units and hardware as reported.\n"
    "- Set claimed_by_authors=false for numbers quoted from OTHER papers (baselines/"
    "comparisons), true for the paper's own results.\n"
    "- BE CONCISE: report only this paper's headline results — at most ~15 benchmark rows "
    "and ~6 model variants (the proposed method + key baselines). Keep every 'notes' field "
    "under 12 words; omit notes if not needed.\n"
    "- Empty lists are fine if the paper reports no quantitative results.")


def run(cfg: Config, client: LLMClient, conn: sqlite3.Connection,
        limit: int | None = None) -> int:
    cap = limit or int(cfg.get("constants.analyze_cap", 40))
    todo = ps.needs_extract(conn, limit=cap)
    log.info("extracting benchmarks for %d core papers (cap=%d)", len(todo), cap)
    done = 0
    for row in todo:
        links = json.loads(row["links_json"] or "{}")
        # 35k chars (~9k tokens) comfortably covers intro+results+tables while staying fast.
        text = pdf.get_text(cfg, row["id"], links.get("pdf") or "", max_chars=35000)
        body = text or row["abstract"] or ""
        user = (f"Title: {row['title']}\n\nAbstract: {row['abstract'] or ''}\n\n"
                f"Paper text (may be truncated):\n{body}")
        try:
            res = client.complete_json("extract", SYSTEM, user, ExtractionResult,
                                       label="extract", max_tokens=12000)
        except Exception as e:  # noqa: BLE001
            log.warning("extract failed for %s: %s", row["id"], e)
            continue
        n_models, n_rows = bm.store_extraction(conn, row["id"], res.models, res.benchmarks)
        done += 1
        log.debug("%s -> %d variants, %d benchmark rows", row["id"], n_models, n_rows)
        conn.commit()
    log.info("extracted benchmarks from %d papers", done)
    return done
