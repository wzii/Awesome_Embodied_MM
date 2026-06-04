"""Streamlit Q&A app — the WAM knowledge base front-end (long-context, no RAG).

Run locally:   streamlit run src/wam/webapp/app.py
On HF Spaces:  set OPENROUTER_API_KEY as a Space secret; this file is the entry point.

The OpenRouter key stays server-side. Answers are grounded in a knowledge pack built from the
committed data/wam.db (paper summaries + scores + leaderboard + authors + trends).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import streamlit as st  # noqa: E402

from wam.config import load_config  # noqa: E402
from wam.webapp.qa import answer  # noqa: E402

st.set_page_config(page_title="Awesome-WAM Knowledge Base", page_icon="🤖", layout="centered")
st.title("🤖 Awesome-WAM Knowledge Base")
st.caption("Ask about World Action Models — papers, benchmarks, authors, trends. "
           "Answers are grounded in the tracked corpus and cite paper ids.")

cfg = load_config()
db_exists = cfg.path("db").exists()
if not db_exists:
    st.warning("No data found yet. Run the pipeline to populate data/wam.db.")

examples = ["Which VLA models report real-time inference?",
            "What are the rising research directions?",
            "Who works on world models for autonomous driving?"]
q = st.text_input("Your question", placeholder=examples[0])
st.caption("Try: " + " · ".join(f"_{e}_" for e in examples))

if q and db_exists:
    with st.spinner("Reading the corpus and composing an answer…"):
        res = answer(q, cfg=cfg)
    st.markdown(res["answer"])
    st.caption(f"Grounded in a {res['pack_chars']:,}-char knowledge pack.")
