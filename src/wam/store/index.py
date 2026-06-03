"""Local embeddings + FAISS index for the RAG knowledge base.

Embeds every paper (ALL tracks, including dropped — they stay searchable per project policy)
plus influential-author cards, using a local sentence-transformers model (free). The index +
a parallel metadata file are written under ``data/index/`` and committed so the web app can
load them directly. Also exposes ``embed_texts`` for the trends clustering stage.
"""

from __future__ import annotations

import json
import sqlite3
from functools import lru_cache
from pathlib import Path

from wam.config import Config
from wam.logging import get_logger

log = get_logger("store.index")


@lru_cache(maxsize=2)
def get_embedder(model_name: str):
    from sentence_transformers import SentenceTransformer
    log.info("loading embedder %s", model_name)
    return SentenceTransformer(model_name)


def embed_texts(cfg: Config, texts: list[str]):
    import numpy as np
    model = get_embedder(cfg.get("rag.embed_model", "BAAI/bge-small-en-v1.5"))
    vecs = model.encode(texts, normalize_embeddings=True, show_progress_bar=False,
                        batch_size=64)
    return np.asarray(vecs, dtype="float32")


def _records(cfg: Config, conn: sqlite3.Connection) -> list[dict]:
    """Build the corpus: papers (all tracks unless disabled) + author cards."""
    recs: list[dict] = []
    include_drop = bool(cfg.get("rag.index_dropped", True))
    where = "" if include_drop else "WHERE track != 'drop'"
    for r in conn.execute(f"SELECT id, title, abstract, track, links_json, summary_json, "
                          f"analysis_json, innovation_json FROM papers {where}"):
        parts = [r["title"] or "", r["abstract"] or ""]
        for col in ("summary_json", "analysis_json", "innovation_json"):
            if r[col]:
                parts.append(" ".join(str(v) for v in json.loads(r[col]).values()))
        links = json.loads(r["links_json"] or "{}")
        recs.append({"ref_id": r["id"], "kind": f"paper:{r['track']}", "title": r["title"],
                     "url": links.get("abs") or links.get("pdf") or "",
                     "text": "\n".join(p for p in parts if p)[:4000]})
    for r in conn.execute("SELECT id, name, directions, s2_url, paper_ids_json FROM authors"):
        recs.append({"ref_id": f"author:{r['id']}", "kind": "author", "title": r["name"],
                     "url": r["s2_url"] or "",
                     "text": f"{r['name']} — research directions: {r['directions'] or ''}"})
    return recs


def build_index(cfg: Config, conn: sqlite3.Connection) -> int:
    import faiss
    recs = _records(cfg, conn)
    if not recs:
        log.warning("no records to index")
        return 0
    vecs = embed_texts(cfg, [r["text"] for r in recs])
    index = faiss.IndexFlatIP(vecs.shape[1])
    index.add(vecs)
    out = cfg.path("index_dir")
    out.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(out / "faiss.index"))
    with open(out / "meta.jsonl", "w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps({k: r[k] for k in ("ref_id", "kind", "title", "url")}) + "\n")
    (out / "texts.jsonl").write_text(
        "\n".join(json.dumps({"ref_id": r["ref_id"], "text": r["text"]}) for r in recs),
        encoding="utf-8")
    log.info("built FAISS index: %d vectors (dim %d) -> %s", len(recs), vecs.shape[1], out)
    return len(recs)


def load_index(cfg: Config):
    """Return (faiss_index, meta_list, texts_by_ref) for querying."""
    import faiss
    out = cfg.path("index_dir")
    index = faiss.read_index(str(out / "faiss.index"))
    meta = [json.loads(l) for l in (out / "meta.jsonl").read_text(encoding="utf-8").splitlines()]
    texts = {}
    for l in (out / "texts.jsonl").read_text(encoding="utf-8").splitlines():
        d = json.loads(l)
        texts[d["ref_id"]] = d["text"]
    return index, meta, texts


def search(cfg: Config, query: str, k: int | None = None) -> list[dict]:
    index, meta, texts = load_index(cfg)
    k = k or int(cfg.get("rag.top_k", 8))
    qv = embed_texts(cfg, [query])
    scores, idxs = index.search(qv, min(k, len(meta)))
    hits = []
    for score, i in zip(scores[0], idxs[0]):
        if i < 0:
            continue
        m = dict(meta[i])
        m["score"] = float(score)
        m["text"] = texts.get(m["ref_id"], "")
        hits.append(m)
    return hits
