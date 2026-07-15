"""
Project management service.
"""

from __future__ import annotations

import json
import shutil
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
    """
    Service responsible for managing projects.
    """

    def __init__(self) -> None:

        PROJECT_ROOT.mkdir(
            parents=True,
            exist_ok=True,
        )

    def create(
        self,
        name: str,
    ) -> Project:

        project = Project.create(name)

        folder = PROJECT_ROOT / project.slug

        if folder.exists():

            raise FileExistsError(
                f"Project '{project.slug}' already exists."
            )

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        for directory in PROJECT_STRUCTURE:

            (
                folder / directory
            ).mkdir(
                parents=True,
                exist_ok=True,
            )

        project.save(folder)

        return project

    def list(
        self,
    ) -> list[Project]:

        projects: list[Project] = []

        for metadata in PROJECT_ROOT.glob(
            "*/project.json"
        ):

            with metadata.open(
                "r",
                encoding="utf-8",
            ) as fp:

                data = json.load(fp)

            projects.append(
                Project(**data)
            )

        return sorted(
            projects,
            key=lambda p: p.created_at,
            reverse=True,
        )

    def get(
        self,
        slug: str,
    ) -> Project:

        metadata = (
            PROJECT_ROOT
            / slug
            / "project.json"
        )

        if not metadata.exists():

            raise FileNotFoundError(
                slug
            )

        with metadata.open(
            "r",
            encoding="utf-8",
        ) as fp:

            data = json.load(fp)

        return Project(**data)

    def exists(
        self,
        slug: str,
    ) -> bool:

        return (
            PROJECT_ROOT / slug
        ).exists()

    def rename(
        self,
        slug: str,
        new_name: str,
    ) -> Project:

        project = self.get(slug)

        new_name = new_name.strip()

        if not new_name:
            raise ValueError(
                "Project name cannot be empty."
            )

        project.name = new_name

        folder = PROJECT_ROOT / slug

        project.save(folder)

        return project

    def delete(
        self,
        slug: str,
    ) -> None:

        folder = (
            PROJECT_ROOT / slug
        )

        if not folder.exists():

            raise FileNotFoundError(
                slug
            )

        shutil.rmtree(folder)


project_service = ProjectService()