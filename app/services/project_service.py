"""
Project management service.
"""

from __future__ import annotations

from pathlib import Path

from app.models.project import Project


ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = ROOT / "workspace" / "projects"


PROJECT_STRUCTURE = (
    "story",
    "prompts",
    "images",
    "audio",
    "video",
    "exports",
    "cache",
    "temp",
)


class ProjectService:
    def __init__(self) -> None:
        PROJECT_ROOT.mkdir(
            parents=True,
            exist_ok=True,
        )

    def create(self, name: str) -> Project:

        project = Project.create(name)

        folder = PROJECT_ROOT / project.slug

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        for directory in PROJECT_STRUCTURE:
            (folder / directory).mkdir(
                exist_ok=True,
            )

        project.save(folder)

        return project

    def list(self) -> list[Project]:

        projects: list[Project] = []

        for project_file in PROJECT_ROOT.glob("*/project.json"):

            import json

            with project_file.open(
                encoding="utf-8",
            ) as fp:

                data = json.load(fp)

            projects.append(Project(**data))

        return sorted(
            projects,
            key=lambda p: p.created_at,
            reverse=True,
        )


project_service = ProjectService()