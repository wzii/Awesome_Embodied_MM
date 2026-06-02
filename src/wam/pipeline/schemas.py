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
