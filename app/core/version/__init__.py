"""
AI Studio version information.

This module provides a single source of truth for application
metadata and semantic versioning.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Version:
    """Application version metadata."""

    major: int
    minor: int
    patch: int
    stage: str = "dev"

    @property
    def short(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    @property
    def full(self) -> str:
        return f"{self.short}-{self.stage}" if self.stage else self.short


APP_NAME = "AI Studio"
APP_DESCRIPTION = "Local AI Video Factory"

VERSION = Version(
    major=0,
    minor=1,
    patch=0,
    stage="alpha",
)

__all__ = [
    "APP_NAME",
    "APP_DESCRIPTION",
    "VERSION",
]