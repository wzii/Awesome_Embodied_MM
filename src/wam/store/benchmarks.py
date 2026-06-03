"""Benchmark + model-variant persistence.

Model identity = (model_name, training_dataset) -> a slugified ``variant_key``, so the same
model name finetuned on a different dataset is tracked as a distinct system. Benchmark rows
are append-and-merge (UNIQUE constraint dedups identical rows) so conflicting numbers from
different papers stay visible side by side.
"""

from __future__ import annotations

import re
import sqlite3
from datetime import date, datetime

from wam.pipeline.schemas import BenchmarkRow, ModelVariant


def variant_key(model_name: str, training_dataset: str | None) -> str:
    base = f"{model_name}|{training_dataset or 'unknown'}".lower()
    return re.sub(r"[^a-z0-9]+", "-", base).strip("-")


def upsert_variant(conn: sqlite3.Connection, v: ModelVariant, source_paper_id: str) -> str:
    vk = variant_key(v.model_name, v.training_dataset)
    conn.execute(
        """INSERT INTO model_variants
           (variant_key, model_name, training_dataset, base_model, params, modality,
            source_paper_id, updated_at)
           VALUES (?,?,?,?,?,?,?,?)
           ON CONFLICT(variant_key) DO UPDATE SET
             base_model=COALESCE(excluded.base_model, base_model),
             params=COALESCE(excluded.params, params),
             modality=COALESCE(excluded.modality, modality),
             updated_at=excluded.updated_at""",
        (vk, v.model_name, v.training_dataset, v.base_model, v.params, v.modality,
         source_paper_id, datetime.now().isoformat(timespec="seconds")),
    )
    return vk


def insert_benchmark(conn: sqlite3.Connection, row: BenchmarkRow, source_paper_id: str) -> None:
    vk = variant_key(row.model_name, row.training_dataset)
    conn.execute(
        """INSERT OR IGNORE INTO benchmarks
           (variant_key, model_name, training_dataset, benchmark, task, split, metric_name,
            metric_value, inference_speed, speed_unit, inference_cost, cost_unit, hardware,
            source_paper_id, claimed_by_authors, notes, extracted_on)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (vk, row.model_name, row.training_dataset, row.benchmark, row.task, row.split,
         row.metric_name, row.metric_value, row.inference_speed, row.speed_unit,
         row.inference_cost, row.cost_unit, row.hardware, source_paper_id,
         int(row.claimed_by_authors), row.notes, date.today().isoformat()),
    )


def store_extraction(conn: sqlite3.Connection, paper_id: str, models: list[ModelVariant],
                     rows: list[BenchmarkRow]) -> tuple[int, int]:
    for v in models:
        upsert_variant(conn, v, paper_id)
    # Ensure any variant referenced by a row exists even if not in `models`.
    seen = {variant_key(v.model_name, v.training_dataset) for v in models}
    for r in rows:
        vk = variant_key(r.model_name, r.training_dataset)
        if vk not in seen:
            upsert_variant(conn, ModelVariant(model_name=r.model_name,
                                              training_dataset=r.training_dataset), paper_id)
            seen.add(vk)
        insert_benchmark(conn, r, paper_id)
    conn.execute("UPDATE papers SET benchmarks_extracted=1 WHERE id=?", (paper_id,))
    return len(models), len(rows)
