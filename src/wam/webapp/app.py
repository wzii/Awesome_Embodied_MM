"""Streamlit RAG Q&A app — the WAM knowledge base front-end.

Run locally:   streamlit run src/wam/webapp/app.py
On HF Spaces:  set OPENROUTER_API_KEY as a Space secret; this file is the entry point.

The OpenRouter key stays server-side. The FAISS index is loaded from data/index/ (committed).
"""

from __future__ import annotations

import sys
from pathlib import Path

# Allow running via `streamlit run` from a checkout.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import streamlit as st  # noqa: E402

from wam.config import load_config  # noqa: E402
from wam.webapp.qa import answer  # noqa: E402

st.set_page_config(page_title="Awesome-WAM Knowledge Base", page_icon="🤖", layout="centered")
st.title("🤖 Awesome-WAM Knowledge Base")
st.caption("Ask about World Action Models — papers, benchmarks, authors. Answers cite sources "
           "from the tracked corpus.")

cfg = load_config()
try:
    idx_dir = cfg.path("index_dir")
    has_index = (idx_dir / "faiss.index").exists()
except Exception:  # noqa: BLE001
    has_index = False

if not has_index:
    st.warning("No index found yet. Run the pipeline's `index` stage to build the knowledge base.")

q = st.text_input("Your question", placeholder="e.g. Which VLA models report real-time inference?")
if q and has_index:
    with st.spinner("Searching the corpus and composing an answer…"):
        res = answer(q, cfg=cfg)
    st.markdown(res["answer"])
    st.divider()
    st.subheader("Sources")
    for s in res["sources"]:
        link = f"[{s['title']}]({s['url']})" if s["url"] else s["title"]
        st.markdown(f"**[{s['n']}]** {link} · _{s['kind']}_ · sim={s['score']}")
