"""
Workspace management.

Creates and validates the AI Studio workspace structure.
"""

from __future__ import annotations

from dataclasses import dataclass, fields
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "workspace"


@dataclass(slots=True, frozen=True)
class WorkspacePaths:
    cache: Path
    downloads: Path
    exports: Path
    logs: Path
    models: Path
    projects: Path
    temp: Path


class WorkspaceManager:
    def __init__(self) -> None:
        self.paths = WorkspacePaths(
            cache=WORKSPACE / "cache",
            downloads=WORKSPACE / "downloads",
            exports=WORKSPACE / "exports",
            logs=WORKSPACE / "logs",
            models=WORKSPACE / "models",
            projects=WORKSPACE / "projects",
            temp=WORKSPACE / "temp",
        )

    def initialize(self) -> None:
        WORKSPACE.mkdir(parents=True, exist_ok=True)

        for field in fields(self.paths):
            path: Path = getattr(self.paths, field.name)
            path.mkdir(parents=True, exist_ok=True)


workspace = WorkspaceManager()