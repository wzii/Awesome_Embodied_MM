"""Shared Pydantic models.

``PaperRecord`` is the normalized in-memory shape produced by the fetch sources and stored
in the ``papers`` table. LLM output schemas (summary, analysis, scores, ...) are added in
later phases next to the stages that use them.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class Links(BaseModel):
    abs: str | None = None
    pdf: str | None = None
    project_page: str | None = None
    code: str | None = None
    doi: str | None = None


class PaperRecord(BaseModel):
    """A fetched, source-normalized item (paper or news) before any LLM processing."""

    id: str = Field(description="stable id, e.g. 'arxiv:2506.01234' or 'news:<sha1>'")
    source: str
    title: str
    authors: list[str] = Field(default_factory=list)
    published: str | None = None          # ISO date
    abstract: str | None = None
    categories: list[str] = Field(default_factory=list)
    links: Links = Field(default_factory=Links)
    citations: int = 0
    influential_citations: int = 0
    has_code: bool = False

    @property
    def arxiv_id(self) -> str | None:
        return self.id.split("arxiv:", 1)[1] if self.id.startswith("arxiv:") else None
