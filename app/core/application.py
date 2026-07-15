"""
Global application state.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from app.models.project import Project


@dataclass(slots=True)
class ApplicationState:
    """
    Holds the current application state.
    """

    started_at: datetime = field(default_factory=datetime.utcnow)

    current_project: Optional[Project] = None

    debug: bool = False

    def open_project(self, project: Project) -> None:
        self.current_project = project

    def close_project(self) -> None:
        self.current_project = None

    @property
    def has_project(self) -> bool:
        return self.current_project is not None


application = ApplicationState()