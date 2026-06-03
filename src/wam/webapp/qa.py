"""RAG question-answering core (UI-agnostic).

Retrieves from the FAISS index and asks the Q&A-tier model to answer using ONLY the retrieved
context, with inline [n] citations that map to sources. Kept separate from the Streamlit UI so
it can be unit-tested / reused.
"""

from __future__ import annotations

from wam.config import Config, load_config
from wam.llm import LLMClient
from wam.logging import get_logger
from wam.store import index as idx

log = get_logger("webapp.qa")

SYSTEM = (
    "You answer questions about World Action Models research using ONLY the provided sources. "
    "Cite sources inline as [n] matching the source numbers. If the sources don't contain the "
    "answer, say so. Be concise and concrete; never invent papers or numbers.")


def answer(question: str, cfg: Config | None = None, client: LLMClient | None = None,
           k: int | None = None) -> dict:
    cfg = cfg or load_config()
    client = client or LLMClient(cfg)
    hits = idx.search(cfg, question, k=k)
    if not hits:
        return {"answer": "The knowledge base is empty or no relevant sources were found.",
                "sources": []}
    context = "\n\n".join(
        f"[{i+1}] ({h['kind']}) {h['title']}\n{h['text'][:1200]}" for i, h in enumerate(hits))
    ans = client.complete("qa", SYSTEM, f"Question: {question}\n\nSources:\n{context}",
                          label="qa", max_tokens=2000)
    sources = [{"n": i + 1, "title": h["title"], "url": h["url"], "kind": h["kind"],
                "score": round(h["score"], 3)} for i, h in enumerate(hits)]
    return {"answer": ans, "sources": sources}
