# Awesome-Embodied&MM — Setup & Operations

## Secrets

### GitHub repo secrets (Settings → Secrets and variables → Actions)
Required for the daily workflow (`.github/workflows/daily.yml`):

| Secret | Purpose |
|--------|---------|
| `OPENROUTER_API_KEY` | LLM calls (filter/summarize/analyze/extract/score/trends) |
| `GMAIL_USER` | Gmail address that sends the digest |
| `GMAIL_APP_PASSWORD` | Gmail **app password** (not your login password) — see below |
| `SUBSCRIBERS` | Recipient list, comma-separated or JSON array. **Never commit this.** |
| `SEMANTIC_SCHOLAR_API_KEY` | *(optional)* higher S2 rate limits |
| `HF_TOKEN` | *(optional)* push the daily DB to the HF Space (keeps chat/dashboard fresh) |
| `HF_SPACE` *(repo **variable**, not secret)* | e.g. `HardToFindAGoodUserName/Awesome_Embodied_MM` |

### Gmail app password
1. Enable 2-Step Verification on the Google account.
2. Google Account → Security → App passwords → generate one for "Mail".
3. Use that 16-char value as `GMAIL_APP_PASSWORD`. Gmail SMTP: `smtp.gmail.com:465` (SSL).

## Local development
```bash
python -m venv .venv && . .venv/bin/activate
pip install -e .   # no embeddings/vector DB needed (Q&A is long-context)
cp .env.example .env   # fill OPENROUTER_API_KEY (+ GMAIL_*/SUBSCRIBERS to test email)

# Run stages (idempotent, resumable). --limit caps LLM stages for quick tests.
python scripts/run_local.py --stages fetch
python scripts/run_local.py --stages filter,summarize,analyze,extract,score,innovation --limit 20
python scripts/run_local.py --stages people,trends,render
WAM_DEBUG=1 python scripts/run_local.py            # full pipeline, full trace to logs/
python scripts/run_local.py --stages email --email-test you@example.com   # test send to self
```

## Knowledge-base web app (Hugging Face Space)
- Create a **Streamlit** Space; point it at this repo (or sync `src/wam`, `config/`,
  `data/wam.db`, `requirements.txt`).
- Set the Space secret `OPENROUTER_API_KEY` (stays server-side).
- Entry point: `src/wam/webapp/app.py` (`streamlit run src/wam/webapp/app.py`).
- Q&A is **long-context, no embeddings**: it builds a knowledge pack from the committed
  `data/wam.db` (summaries + scores + leaderboard + authors + trends) and answers with
  citations. Dropped papers are included (title-only) so the KB still covers them.

## Scheduling
The daily workflow runs at 13:00 UTC and on manual dispatch. It commits results back to the
repo in two checkpoints (data, then README+index) so a late failure never loses earlier work,
then sends the email last.

## Tuning (`config/config.yaml`)
- `models.tiers` / `stage_tiers`: which OpenRouter model each stage uses.
- `constants.analyze_cap`: max papers deeply analyzed/scored per run (cost guard).
- `scoring.*_weights`: rubric weights (top-4 WAM metrics weighted 2×).
- `config/profile.md`: the WAM definition + scoring guidance the prompts read.
