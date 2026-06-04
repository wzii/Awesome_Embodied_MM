"""Build + send the daily digest email via Gmail SMTP.

Clean and scannable: the key points (counts, what's hot, top picks) sit above the fold, with
compact cards and obvious links. The recipient list lives in the ``SUBSCRIBERS`` env var
(comma-separated or a JSON array) and is NEVER committed. Uses inline CSS for client support.
"""

from __future__ import annotations

import json
import os
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


def _wt(row) -> float:
    try:
        return float(json.loads(row["scores_json"]).get("weighted_total") or 0)
    except Exception:  # noqa: BLE001
        return 0.0


def _score_badge(v) -> str:
    return (f'<span style="background:#1a4fcc;color:#fff;border-radius:4px;padding:1px 6px;'
            f'font-size:12px;margin-left:6px">{v}</span>')


def _card(row) -> str:
    """Detailed featured card: title link + score badge + one-line tldr."""
    s = json.loads(row["scores_json"])
    tldr = json.loads(row["summary_json"] or "{}").get("tldr", "")
    link = (_links(row["links_json"]).get("abs") or _links(row["links_json"]).get("pdf") or "#")
    return (f'<div style="margin:10px 0 14px">'
            f'<a href="{link}" style="font-weight:600;color:#1a4fcc;text-decoration:none;'
            f'font-size:14px">{row["title"]}</a>{_score_badge(s.get("weighted_total","?"))}'
            f'<div style="font-size:13px;color:#333;margin-top:3px">{tldr}</div></div>')


def _compact(row) -> str:
    """Compact grouped-tier item: score + title link + short description."""
    s = json.loads(row["scores_json"])
    tldr = json.loads(row["summary_json"] or "{}").get("tldr", "")
    if len(tldr) > 160:
        tldr = tldr[:160].rsplit(" ", 1)[0].rstrip(".,;: ") + "…"
    link = (_links(row["links_json"]).get("abs") or _links(row["links_json"]).get("pdf") or "#")
    desc = f' — <span style="color:#444">{tldr}</span>' if tldr else ""
    return (f'<div style="font-size:13px;margin:4px 0">'
            f'<b>{s.get("weighted_total","?")}</b> · '
            f'<a href="{link}" style="color:#1a4fcc;text-decoration:none">{row["title"]}</a>'
            f'{desc}</div>')


def build_html(cfg: Config, conn: sqlite3.Connection, today: str | None = None) -> tuple[str, str]:
    today = today or date.today().isoformat()
    counts = dict(conn.execute("SELECT track, count(*) FROM papers GROUP BY track").fetchall())
    new_core = conn.execute(
        "SELECT count(*) FROM papers WHERE track='core' AND first_seen=?", (today,)).fetchone()[0]

    # Core papers: new today; fall back to recent if none new.
    sel = ("SELECT id, title, links_json, scores_json, summary_json FROM papers WHERE "
           "track='core' AND scores_json IS NOT NULL")
    order = " ORDER BY json_extract(scores_json,'$.weighted_total') DESC"
    rows = conn.execute(sel + " AND first_seen=?" + order, (today,)).fetchall()
    fallback = not rows
    if fallback:
        rows = conn.execute(sel + order + " LIMIT 60").fetchall()

    snap = conn.execute("SELECT max(snapshot_date) FROM fronts").fetchone()[0]
    hot = conn.execute(
        "SELECT name, size, momentum FROM fronts WHERE snapshot_date=? AND momentum='rising' "
        "ORDER BY size DESC LIMIT 5", (snap,)).fetchall() if snap else []
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
    parts.append(f'<h1 style="font-size:20px;margin:0 0 4px">🤖 WAM Daily — {today}</h1>')
    parts.append(f'<p style="color:#666;font-size:13px;margin:0 0 16px">'
                 f'{new_core} new core papers today · {counts.get("core",0)} core / '
                 f'{counts.get("adjacent",0)} adjacent tracked</p>')
    if hot:
        chips = " ".join(
            f'<span style="background:#eef;border-radius:12px;padding:2px 10px;font-size:12px;'
            f'margin-right:6px">📈 {h["name"]} ({h["size"]})</span>' for h in hot)
        parts.append(f'<p style="font-size:13px;margin:0 0 16px"><b>What\'s hot:</b> {chips}</p>')

    # Tier 1 — featured (detailed cards)
    label = "Top recent papers" if fallback else "Top new papers today"
    parts.append(f'<h2 style="font-size:15px;border-bottom:1px solid #eee;padding-bottom:4px">'
                 f'⭐ {label} (score ≥ {feat_thr:g})</h2>')
    if not featured:
        parts.append('<p style="font-size:13px;color:#666">Nothing above the feature threshold '
                     '— see the rest below.</p>')
    parts.extend(_card(r) for r in featured)

    # Tier 2 — the rest, grouped by research direction
    if rest:
        parts.append('<h2 style="font-size:15px;border-bottom:1px solid #eee;padding-bottom:4px;'
                     'margin-top:18px">More core papers</h2>')
        if bool(cfg.get("email.group_lower_by_direction", True)):
            groups: dict[str, list] = {}
            for r in rest:
                groups.setdefault(dir_of.get(r["id"], "Other"), []).append(r)
            for gname in sorted(groups, key=lambda k: (k == "Other", -len(groups[k]))):
                parts.append(f'<p style="font-weight:600;font-size:13px;margin:12px 0 2px">'
                             f'{gname} <span style="color:#999;font-weight:400">'
                             f'({len(groups[gname])})</span></p>')
                parts.extend(_compact(r) for r in groups[gname])
        else:
            parts.extend(_compact(r) for r in rest)
    parts.append(f'<p style="color:#999;font-size:12px;margin-top:20px">Awesome-WAM · '
                 f'<a href="https://github.com/your-org/Awesome-WAM">repo</a></p></div>')
    subject = f"WAM Daily — {today}: {new_core} new" + ("" if not fallback else " (recap)")
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
