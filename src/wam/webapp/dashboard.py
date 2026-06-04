"""Database dashboard — visual browse of the Awesome-Embodied&MM corpus (Streamlit).

Read-only views over data/wam.db: headline metrics, research directions (chart), top scored
papers with their two-layer dimensions, the benchmark leaderboard, and influential authors.
"""

from __future__ import annotations

import json
import sqlite3

import pandas as pd
import streamlit as st

from wam.config import Config

_WAM_TOP4 = [("inference_speed", "spd"), ("generalist", "gen"),
             ("specialist", "spec"), ("inference_cost", "cost")]


def _conn(cfg: Config) -> sqlite3.Connection:
    return sqlite3.connect(f"file:{cfg.path('db')}?mode=ro", uri=True)


def render(cfg: Config) -> None:
    con = _conn(cfg)

    counts = dict(con.execute("SELECT track, count(*) FROM papers GROUP BY track").fetchall())
    nbench = con.execute("SELECT count(*) FROM benchmarks").fetchone()[0]
    nvar = con.execute("SELECT count(*) FROM model_variants").fetchone()[0]
    nauth = con.execute("SELECT count(*) FROM authors").fetchone()[0]
    c = st.columns(6)
    c[0].metric("Core", counts.get("core", 0))
    c[1].metric("Adjacent", counts.get("adjacent", 0))
    c[2].metric("News", counts.get("news", 0))
    c[3].metric("Benchmark rows", nbench)
    c[4].metric("Model variants", nvar)
    c[5].metric("Authors", nauth)

    # --- Research directions ---
    st.subheader("📈 Research directions")
    fronts = pd.read_sql_query(
        "SELECT name, size, momentum, summary FROM fronts WHERE snapshot_date="
        "(SELECT max(snapshot_date) FROM fronts) ORDER BY size DESC", con)
    if not fronts.empty:
        st.bar_chart(fronts.set_index("name")["size"], height=320)
        st.dataframe(fronts, use_container_width=True, hide_index=True)
    else:
        st.info("No trend snapshot yet.")

    # --- Top papers ---
    st.subheader("🏆 Top scored papers")
    track = st.selectbox("Track", ["core", "adjacent", "all"], index=0)
    where = "" if track == "all" else f"AND track='{track}'"
    rows = con.execute(
        f"SELECT id, title, track, published, relevance, scores_json, links_json FROM papers "
        f"WHERE scores_json IS NOT NULL {where} "
        f"ORDER BY json_extract(scores_json,'$.weighted_total') DESC LIMIT 200").fetchall()
    recs = []
    for pid, title, trk, pub, rel, sj, lj in rows:
        s = json.loads(sj or "{}")
        wam = s.get("wam", {})
        links = json.loads(lj or "{}")
        rec = {"score": s.get("weighted_total"), "title": title, "track": trk,
               "published": pub}
        for key, lbl in _WAM_TOP4:
            v = wam.get(key)
            rec[lbl] = v if isinstance(v, int) else None
        rec["code"] = links.get("code") or ""
        rec["abs"] = links.get("abs") or ""
        recs.append(rec)
    if recs:
        df = pd.DataFrame(recs)
        st.dataframe(df, use_container_width=True, hide_index=True, column_config={
            "abs": st.column_config.LinkColumn("abs"),
            "code": st.column_config.LinkColumn("code")})
        st.caption("Score = weighted total. spd/gen/spec/cost = top-4 WAM dims (blank = N/A).")
    else:
        st.info("No scored papers for this track yet.")

    # --- Benchmark leaderboard ---
    st.subheader("📊 Benchmark leaderboard")
    bench = pd.read_sql_query(
        "SELECT benchmark, task, model_name AS model, training_dataset AS trained_on, "
        "metric_name AS metric, metric_value AS value, "
        "CASE claimed_by_authors WHEN 1 THEN 'authors' ELSE '3rd-party' END AS source "
        "FROM benchmarks WHERE metric_value IS NOT NULL ORDER BY benchmark, value DESC", con)
    if not bench.empty:
        st.caption("Model identity = (model, training data) — same name on different data is a "
                   "distinct row.")
        st.dataframe(bench, use_container_width=True, hide_index=True)
    else:
        st.info("No benchmark rows yet.")

    # --- Authors ---
    st.subheader("👥 Influential authors")
    arows = con.execute(
        "SELECT name, citations, h_index, paper_ids_json, directions, s2_url FROM authors "
        "ORDER BY json_array_length(paper_ids_json) DESC").fetchall()
    if arows:
        adf = pd.DataFrame([{
            "author": n, "papers": len(json.loads(pj or "[]")), "citations": cit,
            "h_index": h, "directions": (d or "")[:200], "s2": url or ""}
            for n, cit, h, pj, d, url in arows])
        st.dataframe(adf, use_container_width=True, hide_index=True,
                     column_config={"s2": st.column_config.LinkColumn("s2")})
    else:
        st.info("No authors yet.")
