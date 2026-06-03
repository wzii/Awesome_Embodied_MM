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


def build_html(cfg: Config, conn: sqlite3.Connection, today: str | None = None) -> tuple[str, str]:
    today = today or date.today().isoformat()
    counts = dict(conn.execute("SELECT track, count(*) FROM papers GROUP BY track").fetchall())
    new_core = conn.execute(
        "SELECT count(*) FROM papers WHERE track='core' AND first_seen=?", (today,)).fetchone()[0]

    # Top picks: new core today; fall back to top recent core if none new.
    picks = conn.execute(
        "SELECT title, links_json, scores_json, summary_json FROM papers WHERE track='core' "
        "AND scores_json IS NOT NULL AND first_seen=? "
        "ORDER BY json_extract(scores_json,'$.weighted_total') DESC LIMIT 8", (today,)).fetchall()
    fallback = not picks
    if fallback:
        picks = conn.execute(
            "SELECT title, links_json, scores_json, summary_json FROM papers WHERE track='core' "
            "AND scores_json IS NOT NULL "
            "ORDER BY json_extract(scores_json,'$.weighted_total') DESC LIMIT 8").fetchall()

    snap = conn.execute("SELECT max(snapshot_date) FROM fronts").fetchone()[0]
    hot = conn.execute(
        "SELECT name, size, momentum FROM fronts WHERE snapshot_date=? AND momentum='rising' "
        "ORDER BY size DESC LIMIT 5", (snap,)).fetchall() if snap else []

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

    heading = "Top recent papers" if fallback else "Top new papers today"
    parts.append(f'<h2 style="font-size:15px;border-bottom:1px solid #eee;padding-bottom:4px">'
                 f'{heading}</h2>')
    for r in picks:
        s = json.loads(r["scores_json"])
        tldr = json.loads(r["summary_json"] or "{}").get("tldr", "")
        links = _links(r["links_json"])
        link = links.get("abs") or links.get("pdf") or "#"
        parts.append(
            f'<div style="margin:10px 0 14px">'
            f'<a href="{link}" style="font-weight:600;color:#1a4fcc;text-decoration:none;'
            f'font-size:14px">{r["title"]}</a>'
            f'<span style="background:#1a4fcc;color:#fff;border-radius:4px;padding:1px 6px;'
            f'font-size:12px;margin-left:6px">{s.get("weighted_total","?")}</span>'
            f'<div style="font-size:13px;color:#333;margin-top:3px">{tldr}</div></div>')
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
