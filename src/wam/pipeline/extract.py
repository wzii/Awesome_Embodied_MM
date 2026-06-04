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
    "Extract structured experimental results from this embodied-AI / World-Action-Model paper. "
    "Rules:\n"
    "- Only report numbers ACTUALLY stated in the text — never estimate or invent.\n"
    "- Use the benchmark's STANDARD NAME and the variant when given, e.g. LIBERO, LIBERO-Long, "
    "LIBERO-Goal, CALVIN (ABC->D), RoboTwin, SimplerEnv, RLBench, Meta-World, ManiSkill, "
    "RoboCasa, Open-X, ALFWorld, VBench/VBench-Long. NEVER use a table caption ('Table 2'), a "
    "section title, or a single task name ('Put Cube into Cup') as the benchmark — those tasks "
    "go in the 'task' field, with the benchmark in 'benchmark'.\n"
    "- Prefer the HEADLINE/aggregate number per (model, benchmark) (e.g. overall success rate "
    "/ average), not every per-task row. Avoid generic names like 'Average' or 'Table N'.\n"
    "- Each model is identified by (model_name, training_dataset). The SAME name trained/"
    "finetuned on a different dataset is a DIFFERENT variant — capture the training dataset.\n"
    "- Give metric name+value and any inference speed/cost with units + hardware as reported.\n"
    "- claimed_by_authors=false for numbers quoted from OTHER papers (baselines), true for the "
    "paper's own results.\n"
    "- BE CONCISE: at most ~15 rows and ~8 model variants (proposed method + key baselines on "
    "the main benchmarks). Notes under 12 words or omit. Empty lists are fine.")


def _extract_one(cfg: Config, client: LLMClient, row) -> tuple[str, object | None]:
    """Worker: fetch PDF text + extract. Returns (paper_id, ExtractionResult|None). No DB."""
    links = json.loads(row["links_json"] or "{}")
    text = pdf.get_text(cfg, row["id"], links.get("pdf") or "", max_chars=35000)
    body = text or row["abstract"] or ""
    user = (f"Title: {row['title']}\n\nAbstract: {row['abstract'] or ''}\n\n"
            f"Paper text (may be truncated):\n{body}")
    try:
        res = client.complete_json("extract", SYSTEM, user, ExtractionResult,
                                   label="extract", max_tokens=6000)
        return row["id"], res
    except Exception as e:  # noqa: BLE001
        log.warning("extract failed for %s: %s", row["id"], e)
        return row["id"], None


def run(cfg: Config, client: LLMClient, conn: sqlite3.Connection,
        limit: int | None = None) -> int:
    from concurrent.futures import ThreadPoolExecutor, as_completed
    cap = limit or int(cfg.get("constants.analyze_cap", 40))
    todo = ps.needs_extract(conn, limit=cap)
    workers = int(cfg.get("constants.extract_workers", 6))
    log.info("extracting benchmarks for %d papers (%d workers)", len(todo), workers)
    done = 0
    # LLM calls run concurrently (I/O-bound); each result is committed in the main thread AS
    # IT COMPLETES (as_completed, not map) so a slow/stuck paper never blocks committing others.
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(_extract_one, cfg, client, r): r["id"] for r in todo}
        for fut in as_completed(futs):
            pid, res = fut.result()
            if res is not None:
                bm.store_extraction(conn, pid, res.models, res.benchmarks)
            else:
                conn.execute("UPDATE papers SET benchmarks_extracted=1 WHERE id=?", (pid,))
            conn.commit()
            done += 1
            if done % 20 == 0:
                log.info("extract progress: %d/%d", done, len(todo))
    log.info("extracted benchmarks from %d papers", done)
    return done
