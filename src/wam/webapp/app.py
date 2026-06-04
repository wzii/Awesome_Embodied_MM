"""Streamlit app — Awesome-Embodied&MM: a chat assistant + a database dashboard.

Two views (sidebar): 💬 Chat (multi-turn, long-context Q&A grounded in the corpus + live web
search) and 📊 Database (visual browse of papers, scores, benchmarks, directions, authors).

Run locally:   streamlit run src/wam/webapp/app.py
On HF Spaces:  set OPENROUTER_API_KEY as a Space secret; this file is the entry point.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import streamlit as st  # noqa: E402

from wam.config import load_config  # noqa: E402

st.set_page_config(page_title="Awesome-Embodied&MM", page_icon="🤖", layout="wide")
cfg = load_config()
db_exists = cfg.path("db").exists()

st.sidebar.title("🤖 Awesome-Embodied&MM")
view = st.sidebar.radio("View", ["💬 Chat", "📊 Database"], label_visibility="collapsed")
if not db_exists:
    st.sidebar.warning("No data yet — run the pipeline to populate data/wam.db.")


def _chat() -> None:
    from wam.webapp.qa import answer
    st.title("💬 Chat")
    st.caption("Ask about World Action Models, VLA, world models & video generation. Grounded "
               "in the tracked corpus (cited by paper id) + live web search for original text "
               "and related concepts.")
    with st.sidebar:
        if st.button("🗑 Clear chat"):
            st.session_state.messages = []
            st.rerun()
    st.session_state.setdefault("messages", [])
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
    if q := st.chat_input("Ask a question…", disabled=not db_exists):
        st.session_state.messages.append({"role": "user", "content": q})
        with st.chat_message("user"):
            st.markdown(q)
        with st.chat_message("assistant"):
            with st.spinner("Thinking (corpus + web)…"):
                res = answer(q, history=st.session_state.messages[:-1], cfg=cfg)
            st.markdown(res["answer"])
            web = " + live web" if res.get("web") else ""
            st.caption(f"Grounded in a {res.get('pack_chars', 0):,}-char pack{web}.")
        st.session_state.messages.append({"role": "assistant", "content": res["answer"]})


def _database() -> None:
    from wam.webapp import dashboard
    st.title("📊 Database")
    if db_exists:
        dashboard.render(cfg)
    else:
        st.info("No data yet.")


if view.startswith("💬"):
    _chat()
else:
    _database()
