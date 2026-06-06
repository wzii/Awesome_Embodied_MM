"""Pydantic schemas for LLM pipeline outputs (Phase 3+).

Each stage forces the model to return one of these; the LLM client validates and retries on
malformed output. ``"N/A"`` is allowed for any WAM metric the paper does not address so we
never penalize with a fake 0.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

Track = Literal["core", "adjacent", "drop"]
# Scores are 0-10 ints, or the string "N/A" when unaddressed.
Score = int | Literal["N/A"]


class RelevanceVerdict(BaseModel):
    track: Track = Field(description="core = is a WAM; adjacent = VLA/world-model/video-gen "
                                     "with transferable ideas; drop = unrelated")
    relevance: float = Field(ge=0.0, le=1.0, description="0..1 confidence this matters to WAM")
    reason: str = Field(description="one sentence justification")


class PaperSummary(BaseModel):
    tldr: str = Field(description="one-sentence takeaway")
    problem: str
    method: str
    results: str


class PaperAnalysis(BaseModel):
    contributions: list[str] = Field(description="key contributions, most important first")
    limitations: list[str]
    wam_relevance: str = Field(description="why this matters for World Action Models")


class GeneralScores(BaseModel):
    novelty: Score
    soundness: Score
    impact: Score


class WAMScores(BaseModel):
    generalist: Score
    inference_speed: Score
    specialist: Score
    inference_cost: Score
    trustworthiness: Score
    collaborative: Score
    controlled_generation: Score
    other: Score


class ScoreCard(BaseModel):
    general: GeneralScores
    wam: WAMScores
    rationale: str = Field(description="brief justification grounded in the paper")


class InnovationNote(BaseModel):
    key_idea: str = Field(description="the core technical innovation")
    transferable_to_wam: str = Field(description="why/how it could transfer to World Action Models")


class InstituteResult(BaseModel):
    """Distinct author affiliations (research institutions / companies) credited on a paper."""
    institutes: list[str] = Field(
        default_factory=list,
        description="full canonical institution/company names from the author block, e.g. "
        "'Google DeepMind', 'Stanford University', 'Tsinghua University', 'NVIDIA'. "
        "Deduplicated. Empty list if none is stated.")


# --- benchmark extraction (Phase 3b) ----------------------------------------
class ModelVariant(BaseModel):
    model_name: str = Field(description="model/system name as called in the paper")
    training_dataset: str | None = Field(
        default=None, description="dataset(s) it was trained/finetuned on — part of its "
        "identity; same name on a different dataset is a different system")
    base_model: str | None = None
    params: str | None = Field(default=None, description="e.g. '7B', '300M'")
    modality: str | None = None


class BenchmarkRow(BaseModel):
    model_name: str
    training_dataset: str | None = None
    benchmark: str = Field(description="benchmark/dataset the result is on")
    task: str | None = None
    split: str | None = None
    metric_name: str | None = Field(default=None, description="e.g. 'success rate', 'accuracy'")
    metric_value: float | None = None
    inference_speed: float | None = Field(default=None, description="numeric value if stated")
    speed_unit: str | None = Field(default=None, description="e.g. 'Hz', 'fps', 'ms', 'tok/s'")
    inference_cost: float | None = None
    cost_unit: str | None = Field(default=None, description="e.g. 'GPU-hours', 'FLOPs', '$'")
    hardware: str | None = Field(default=None, description="hardware as reported, if any")
    claimed_by_authors: bool = Field(
        default=True, description="True if this is the paper's own reported number (vs a "
        "third-party / comparison number quoted from another paper)")
    notes: str | None = None


class ExtractionResult(BaseModel):
    """Only extract numbers ACTUALLY stated in the text. Empty lists are fine."""
    models: list[ModelVariant] = Field(default_factory=list)
    benchmarks: list[BenchmarkRow] = Field(default_factory=list)
