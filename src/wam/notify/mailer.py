"""Build + send the daily digest email via Gmail SMTP.

Clean and scannable: the key points (counts, what's hot, top picks) sit above the fold, with
compact cards and obvious links. The recipient list lives in the ``SUBSCRIBERS`` env var
(comma-separated or a JSON array) and is NEVER committed. Uses inline CSS for client support.
"""

from __future__ import annotations

import json
import os
import re
import smtplib
import sqlite3
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from wam.config import Config
from wam.logging import get_logger

log = get_logger("notify.mailer")


def _subscribers() -> list[str]:
    raw = os.environ.get("SUBSCRIBERS", "").strip()
    if not raw:
        return []
    if raw.startswith("["):
        try:
            return [e.strip() for e in json.loads(raw) if e.strip()]
        except Exception:  # noqa: BLE001
            pass
    return [e.strip() for e in raw.split(",") if e.strip()]


def _links(lj: str | None) -> dict:
    try:
        return json.loads(lj or "{}")
    except Exception:  # noqa: BLE001
        return {}


def _clip(text: str, n: int) -> str:
    text = (text or "").strip()
    if len(text) <= n:
        return text
    return text[:n].rsplit(" ", 1)[0].rstrip(".,;: ") + "…"


_GH = re.compile(r"https?://github\.com/[\w.\-/]+")
_HF = re.compile(r"https?://huggingface\.co/[\w.\-/]+")


def _title_links(links: dict, abstract: str | None) -> str:
    """Small inline links next to a title: code (GitHub), HF, project page, pdf.

    GitHub/HF URLs are pulled from links or, failing that, from the abstract text.
    """
    abstract = abstract or ""
    gh = links.get("code") if (links.get("code") and "github.com" in links["code"]) else None
    if not gh:
        m = _GH.search(abstract)
        gh = m.group(0).rstrip(".)") if m else None
    hf = links.get("hf")
    if not hf:
        if links.get("code") and "huggingface.co" in links["code"]:
            hf = links["code"]
        else:
            m = _HF.search(abstract)
            hf = m.group(0).rstrip(".)") if m else None
    chips = []
    style = 'style="color:#1a4fcc;font-size:11px;text-decoration:none;margin-left:6px"'
    if gh:
        chips.append(f'<a href="{gh}" {style}>⌨ code</a>')
    if hf:
        chips.append(f'<a href="{hf}" {style}>🤗 HF</a>')
    if links.get("project_page"):
        chips.append(f'<a href="{links["project_page"]}" {style}>🔗 page</a>')
    if links.get("pdf"):
        chips.append(f'<a href="{links["pdf"]}" {style}>📄 pdf</a>')
    return "".join(chips)


def _wt(row) -> float:
    try:
        return float(json.loads(row["scores_json"]).get("weighted_total") or 0)
    except Exception:  # noqa: BLE001
        return 0.0


def _score_badge(v) -> str:
    return (f'<span style="background:#1a4fcc;color:#fff;border-radius:4px;padding:1px 6px;'
            f'font-size:12px;margin-left:6px">{v}</span>')


_GEN_LABELS = [("novelty", "nov"), ("soundness", "snd"), ("impact", "imp")]
# WAM order: top-4 (weighted 2x) first, then the rest.
_WAM_LABELS = [("inference_speed", "spd"), ("generalist", "gen"), ("specialist", "spec"),
               ("inference_cost", "cost"), ("trustworthiness", "trust"),
               ("collaborative", "collab"), ("controlled_generation", "ctrl"), ("other", "other")]
_WAM_TOP4 = {"inference_speed", "generalist", "specialist", "inference_cost"}


def _v(x) -> str:
    return str(x) if isinstance(x, int) else "–"


def _chip(label: str, val: str, strong: bool = False) -> str:
    bg, weight = ("#e8f0ff", "600") if strong else ("#f2f2f2", "400")
    return (f'<span style="background:{bg};border-radius:4px;padding:1px 5px;margin:0 4px 2px 0;'
            f'font-size:11px;color:#333;font-weight:{weight};display:inline-block">{label} {val}</span>')


def _metric_badges(scores: dict) -> str:
    """Full two-layer dimension badges (general + all WAM; top-4 WAM emphasized)."""
    g, w = scores.get("general", {}) or {}, scores.get("wam", {}) or {}
    gen = "".join(_chip(l, _v(g.get(k))) for k, l in _GEN_LABELS)
    wam = "".join(_chip(l, _v(w.get(k)), k in _WAM_TOP4) for k, l in _WAM_LABELS)
    return (f'<div style="margin:5px 0 0"><span style="color:#999;font-size:11px">general</span> '
            f'{gen}</div>'
            f'<div style="margin:2px 0 0"><span style="color:#999;font-size:11px">WAM</span> '
            f'{wam}</div>')


def _top4_inline(scores: dict) -> str:
    w = scores.get("wam", {}) or {}
    return " · ".join(f"{l} {_v(w.get(k))}" for k, l in
                      [("inference_speed", "spd"), ("generalist", "gen"),
                       ("specialist", "spec"), ("inference_cost", "cost")])


def _card(row, direction: str | None = None) -> str:
    """Detailed featured card: title (+ links), direction tag, blurb, metrics."""
    s = json.loads(row["scores_json"])
    sm = json.loads(row["summary_json"] or "{}")
    links = _links(row["links_json"])
    link = links.get("abs") or links.get("pdf") or "#"
    tldr = sm.get("tldr", "")
    extra = _clip(" ".join(x for x in (sm.get("method", ""), sm.get("results", "")) if x), 300)
    dir_html = ""
    if direction:
        dir_html = (f'<div style="margin-top:4px"><span style="background:#eef3ff;color:#1a4fcc;'
                    f'border-radius:10px;padding:1px 9px;font-size:11px">📂 {direction}</span>'
                    f'</div>')
    blurb = f'<div style="font-size:13px;color:#333;margin-top:5px">{tldr}</div>'
    if extra:
        blurb += f'<div style="font-size:12px;color:#666;margin-top:3px">{extra}</div>'
    return (f'<div style="margin:12px 0;padding:10px 14px;border-left:3px solid #1a4fcc;'
            f'background:#fafbff;border-radius:0 6px 6px 0">'
            f'<a href="{link}" style="font-weight:600;color:#1a4fcc;text-decoration:none;'
            f'font-size:14px">{row["title"]}</a>{_score_badge(s.get("weighted_total","?"))}'
            f'{_title_links(links, row["abstract"])}'
            f'{dir_html}{blurb}'
            f'<div style="margin-top:6px">{_metric_badges(s)}</div></div>')


def _compact(row) -> str:
    """Compact grouped-tier item: score + title link + short description."""
    s = json.loads(row["scores_json"])
    tldr = json.loads(row["summary_json"] or "{}").get("tldr", "")
    if len(tldr) > 160:
        tldr = tldr[:160].rsplit(" ", 1)[0].rstrip(".,;: ") + "…"
    link = (_links(row["links_json"]).get("abs") or _links(row["links_json"]).get("pdf") or "#")
    desc = f' — <span style="color:#444">{tldr}</span>' if tldr else ""
    return (f'<div style="font-size:13px;margin:5px 0">'
            f'<b>{s.get("weighted_total","?")}</b> · '
            f'<a href="{link}" style="color:#1a4fcc;text-decoration:none">{row["title"]}</a>'
            f'{_title_links(_links(row["links_json"]), row["abstract"])}'
            f'{desc}'
            f'<div style="font-size:11px;color:#888;margin-top:1px">{_top4_inline(s)}</div></div>')


def _teams_html(conn: sqlite3.Connection) -> str:
    """Short closing paragraph on the most influential teams / contributors."""
    groups = conn.execute("SELECT name FROM groups ORDER BY json_array_length(member_ids_json) "
                          "DESC LIMIT 3").fetchall()
    authors = conn.execute("SELECT name, affiliation FROM authors ORDER BY "
                           "json_array_length(paper_ids_json) DESC LIMIT 5").fetchall()
    if not authors and not groups:
        return ""
    if groups:
        body = ", ".join(f"<b>{g['name']}</b>" for g in groups)
        lead = f"Most active groups in the tracked corpus: {body}."
    else:
        body = ", ".join(f"<b>{a['name']}</b>" + (f" ({a['affiliation']})" if a["affiliation"]
                         else "") for a in authors)
        lead = f"Most active contributors right now: {body}."
    return ('<h2 style="font-size:15px;border-bottom:1px solid #eee;padding-bottom:4px;'
            f'margin-top:18px">👥 Influential teams</h2>'
            f'<p style="font-size:13px;color:#444;margin:6px 0 0">{lead}</p>')


def build_html(cfg: Config, conn: sqlite3.Connection, today: str | None = None) -> tuple[str, str]:
    today = today or date.today().isoformat()
    counts = dict(conn.execute("SELECT track, count(*) FROM papers GROUP BY track").fetchall())
    new_core = conn.execute(
        "SELECT count(*) FROM papers WHERE track='core' AND first_seen=?", (today,)).fetchone()[0]

    # Core papers: new today; fall back to recent if none new.
    sel = ("SELECT id, title, abstract, links_json, scores_json, summary_json FROM papers WHERE "
           "track='core' AND scores_json IS NOT NULL")
    order = " ORDER BY json_extract(scores_json,'$.weighted_total') DESC"
    rows = conn.execute(sel + " AND first_seen=?" + order, (today,)).fetchall()
    fallback = not rows
    if fallback:
        rows = conn.execute(sel + order + " LIMIT 60").fetchall()

    snap = conn.execute("SELECT max(snapshot_date) FROM fronts").fetchone()[0]
    # Rising directions, excluding the catch-all "Miscellaneous" bucket.
    hot = conn.execute(
        "SELECT name, size, summary FROM fronts WHERE snapshot_date=? AND momentum='rising' "
        "AND name NOT LIKE '%iscellaneous%' ORDER BY size DESC LIMIT 6", (snap,)).fetchall() \
        if snap else []
    # paper id -> research direction (smaller/more-specific fronts win, via size ASC)
    dir_of: dict[str, str] = {}
    if snap:
        for fr in conn.execute("SELECT name, member_ids_json FROM fronts WHERE "
                               "snapshot_date=? ORDER BY size", (snap,)):
            for pid in json.loads(fr["member_ids_json"] or "[]"):
                dir_of[pid] = fr["name"]

    feat_thr = float(cfg.get("email.feature_threshold", 7.0))
    featured = [r for r in rows if _wt(r) >= feat_thr][: int(cfg.get("email.max_featured", 8))]
    feat_ids = {r["id"] for r in featured}
    rest = [r for r in rows if r["id"] not in feat_ids][: int(cfg.get("email.max_grouped", 40))]

    S = "font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif"
    parts = [f'<div style="max-width:640px;margin:auto;{S};color:#1a1a1a">']
    parts.append(f'<h1 style="font-size:20px;margin:0 0 8px">🤖 Embodied&amp;MM Daily — {today}</h1>')
    new_adj = conn.execute("SELECT count(*) FROM papers WHERE track='adjacent' AND first_seen=?",
                           (today,)).fetchone()[0]
    total_core, total_adj = counts.get("core", 0), counts.get("adjacent", 0)

    def _stat(n, lbl):
        return (f'<td style="text-align:center;padding:8px 6px">'
                f'<div style="font-size:22px;font-weight:700;color:#1a4fcc">{n}</div>'
                f'<div style="font-size:11px;color:#777">{lbl}</div></td>')
    parts.append(
        '<table style="width:100%;border-collapse:collapse;margin:0 0 18px;background:#f5f8ff;'
        'border-radius:8px"><tr>'
        + _stat(new_core + new_adj, "relevant today") + _stat(new_core, "core today")
        + _stat(total_core + total_adj, "relevant total") + _stat(total_core, "core total")
        + '</tr></table>')
    if hot:
        parts.append('<h2 style="font-size:15px;border-bottom:1px solid #eee;'
                     'padding-bottom:4px">📈 What\'s hot</h2>')
        items = "".join(
            f'<div style="font-size:13px;margin:5px 0"><b>{h["name"]}</b> '
            f'<span style="color:#999">({h["size"]})</span> — '
            f'<span style="color:#444">{_clip(h["summary"] or "", 160)}</span></div>'
            for h in hot)
        parts.append(items)

    # Tier 1 — featured (detailed cards)
    label = "Top recent papers" if fallback else "Top new papers today"
    parts.append(f'<h2 style="font-size:15px;border-bottom:1px solid #eee;padding-bottom:4px">'
                 f'⭐ {label} (score ≥ {feat_thr:g})</h2>')
    if not featured:
        parts.append('<p style="font-size:13px;color:#666">Nothing above the feature threshold '
                     '— see the rest below.</p>')
    parts.extend(_card(r, dir_of.get(r["id"])) for r in featured)

    # Tier 2 — the rest, grouped by research direction
    if rest:
        parts.append('<h2 style="font-size:15px;border-bottom:1px solid #eee;padding-bottom:4px;'
                     'margin-top:18px">More core papers</h2>')
        if bool(cfg.get("email.group_lower_by_direction", True)):
            groups: dict[str, list] = {}
            for r in rest:
                groups.setdefault(dir_of.get(r["id"], "Other"), []).append(r)
            # Miscellaneous / Other always go last; otherwise larger groups first.
            def _gkey(k):
                last = k == "Other" or "iscellaneous" in k
                return (last, -len(groups[k]))
            for gname in sorted(groups, key=_gkey):
                parts.append(f'<p style="font-weight:600;font-size:13px;margin:12px 0 2px">'
                             f'{gname} <span style="color:#999;font-weight:400">'
                             f'({len(groups[gname])})</span></p>')
                parts.extend(_compact(r) for r in groups[gname])
        else:
            parts.extend(_compact(r) for r in rest)
    parts.append(_teams_html(conn))

    parts.append(
        '<p style="color:#aaa;font-size:11px;margin-top:18px;border-top:1px solid #eee;'
        'padding-top:8px">Dimensions — general: nov=novelty, snd=soundness, imp=impact · '
        'WAM (bold = weighted 2×): spd=inference speed, gen=generalist, spec=specialist, '
        'cost=inference cost, trust=trustworthiness, collab=collaborative, '
        'ctrl=controlled generation. “–” = the paper doesn’t address it.</p>')
    parts.append(f'<p style="color:#999;font-size:12px;margin-top:8px">Awesome-Embodied&amp;MM · '
                 f'<a href="https://github.com/wzii/Awesome_Embodied_MM">repo</a></p></div>')
    subject = f"Embodied&MM Daily — {today}: {new_core} new" + ("" if not fallback else " (recap)")
    return subject, "".join(parts)


def send(cfg: Config, conn: sqlite3.Connection, today: str | None = None,
         test_to: str | None = None) -> int:
    user = os.environ.get("GMAIL_USER")
    pw = os.environ.get("GMAIL_APP_PASSWORD")
    if not (user and pw):
        log.warning("GMAIL_USER / GMAIL_APP_PASSWORD not set; skipping email send")
        return 0
    recipients = [test_to] if test_to else _subscribers()
    if not recipients:
        log.warning("no SUBSCRIBERS configured; skipping send")
        return 0
    subject, html = build_html(cfg, conn, today)
    msg = MIMEMultipart("alternative")
    msg["Subject"], msg["From"] = subject, user
    msg["To"] = ", ".join(recipients)
    msg.attach(MIMEText("This digest is best viewed as HTML.", "plain"))
    msg.attach(MIMEText(html, "html"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(user, pw)
        server.sendmail(user, recipients, msg.as_string())
    log.info("sent digest to %d recipient(s)", len(recipients))
    return len(recipients)
