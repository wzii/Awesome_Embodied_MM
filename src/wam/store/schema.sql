-- Canonical SQLite store for Awesome-WAM.
-- JSON/markdown exports (README, web app, digests) are generated FROM this DB.

PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

-- One row per discovered item (paper or news).
CREATE TABLE IF NOT EXISTS papers (
    id                     TEXT PRIMARY KEY,         -- e.g. "arxiv:2506.01234", "news:<hash>"
    source                 TEXT NOT NULL,            -- arxiv | semantic_scholar | papers_with_code | news
    title                  TEXT NOT NULL,
    authors_json           TEXT,                     -- JSON array of author names
    published              TEXT,                     -- ISO date
    first_seen             TEXT NOT NULL,            -- ISO date we first ingested it
    abstract               TEXT,
    categories_json        TEXT,                     -- JSON array
    track                  TEXT,                     -- core | adjacent | news | drop (NULL = unfiltered)
    links_json             TEXT,                     -- JSON {abs,pdf,project_page,code,doi}
    citations              INTEGER DEFAULT 0,
    influential_citations  INTEGER DEFAULT 0,
    has_code               INTEGER DEFAULT 0,        -- bool
    relevance              REAL,                     -- 0..1; -1 means scoring failed (retry next run)
    relevance_reason       TEXT,
    summary_json           TEXT,                     -- JSON {tldr,problem,method,results}
    analysis_json          TEXT,                     -- JSON {contributions,limitations,wam_relevance}
    innovation_json        TEXT,                     -- JSON {key_idea,transferable_to_wam} (adjacent)
    scores_json            TEXT,                     -- JSON {general,wam,weighted_total,rationale}
    status                 TEXT DEFAULT 'new',       -- new|filtered|summarized|analyzed|scored|done
    pdf_hash               TEXT,
    benchmarks_extracted   INTEGER DEFAULT 0,        -- bool: benchmark/model extraction done
    updated_at             TEXT
);
CREATE INDEX IF NOT EXISTS idx_papers_track ON papers(track);
CREATE INDEX IF NOT EXISTS idx_papers_published ON papers(published);
CREATE INDEX IF NOT EXISTS idx_papers_status ON papers(status);

-- Normalized benchmark rows. Model identity = (model_name, training_dataset) -> variant_key.
CREATE TABLE IF NOT EXISTS benchmarks (
    id                 INTEGER PRIMARY KEY AUTOINCREMENT,
    variant_key        TEXT NOT NULL,
    model_name         TEXT NOT NULL,
    training_dataset   TEXT,
    benchmark          TEXT NOT NULL,
    task               TEXT,
    split              TEXT,
    metric_name        TEXT,
    metric_value       REAL,
    inference_speed    REAL,
    speed_unit         TEXT,
    inference_cost     REAL,
    cost_unit          TEXT,
    hardware           TEXT,
    source_paper_id    TEXT REFERENCES papers(id),
    claimed_by_authors INTEGER DEFAULT 1,
    notes              TEXT,
    extracted_on       TEXT,
    UNIQUE(variant_key, benchmark, task, metric_name, source_paper_id)
);
CREATE INDEX IF NOT EXISTS idx_bench_variant ON benchmarks(variant_key);

-- Model variant registry (the disambiguated identity).
CREATE TABLE IF NOT EXISTS model_variants (
    variant_key      TEXT PRIMARY KEY,
    model_name       TEXT NOT NULL,
    training_dataset TEXT,
    base_model       TEXT,
    params           TEXT,
    modality         TEXT,
    source_paper_id  TEXT REFERENCES papers(id),
    updated_at       TEXT
);

-- Influential authors.
CREATE TABLE IF NOT EXISTS authors (
    id              TEXT PRIMARY KEY,                -- semantic scholar id or slug
    name            TEXT NOT NULL,
    affiliation     TEXT,
    region          TEXT,                            -- country/region of the affiliation
    s2_url          TEXT,
    citations       INTEGER,
    h_index         INTEGER,
    paper_ids_json  TEXT,                            -- JSON array of tracked paper ids
    directions      TEXT,                            -- LLM summary of research directions
    updated_at      TEXT
);

-- Research groups / labs.
CREATE TABLE IF NOT EXISTS groups (
    id              TEXT PRIMARY KEY,
    name            TEXT NOT NULL,
    affiliation     TEXT,
    member_ids_json TEXT,
    directions      TEXT,
    notable_json    TEXT,                            -- JSON array of notable paper ids
    updated_at      TEXT
);

-- Research fronts (trends), snapshot-versioned.
CREATE TABLE IF NOT EXISTS fronts (
    front_id          TEXT NOT NULL,
    snapshot_date     TEXT NOT NULL,
    name              TEXT,
    summary           TEXT,
    member_ids_json   TEXT,
    size              INTEGER,
    momentum          TEXT,                          -- rising | steady | cooling
    volume_json       TEXT,                          -- per-window counts
    PRIMARY KEY (front_id, snapshot_date)
);
CREATE TABLE IF NOT EXISTS front_lineage (
    current_id    TEXT,
    previous_id   TEXT,
    snapshot_date TEXT,
    relationship  TEXT,                              -- continuation | merge | split | new
    overlap       REAL
);

-- Run audit log.
CREATE TABLE IF NOT EXISTS runs (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    run_date     TEXT,
    stage        TEXT,
    n_in         INTEGER,
    n_out        INTEGER,
    cost_usd     REAL,
    notes        TEXT,
    created_at   TEXT
);
