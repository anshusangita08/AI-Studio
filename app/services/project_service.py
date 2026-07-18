"""
Project management service.
"""

from __future__ import annotations

import json
import shutil
from datetime import UTC, datetime
from pathlib import Path

from app.models.project import Project


ROOT = Path(__file__).resolve().parents[2]

# Default project root location
PROJECT_ROOT = ROOT / "workspace" / "projects"

# Reserved project names that conflict with routes
RESERVED_PROJECT_NAMES = {"new", "delete", "edit", "settings", "story"}


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

    def __init__(self, root: Path | None = None) -> None:
        """Create a new service.

        Args:
            root: Optional custom project root. If ``None`` the default
                :data:`PROJECT_ROOT` is used.
        """
        self.PROJECT_ROOT = root or PROJECT_ROOT
        self.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    def create(
        self,
        name: str,
    ) -> Project:
        # Trim leading and trailing whitespace first
        name = name.strip()

        # Validate that the name is not empty after trimming
        if not name:
            raise ValueError("Project name cannot be empty.")

        # Check for reserved names (case-insensitive)
        clean_name = name.lower()
        if clean_name in RESERVED_PROJECT_NAMES:
            raise ValueError("Project name cannot be a reserved word.")

        project = Project.create(name)
        folder = self.PROJECT_ROOT / project.slug
        if folder.exists():

            raise FileExistsError(
                f"Project '{project.slug}' already exists."
            )

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        for directory in PROJECT_STRUCTURE:
            (folder / directory).mkdir(parents=True, exist_ok=True)

        project.save(folder)

        return project

    def list(
        self,
    ) -> list[Project]:

        projects: list[Project] = []

        for metadata in self.PROJECT_ROOT.glob("*/project.json"):

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

        metadata = (self.PROJECT_ROOT / slug / "project.json")

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

        return (self.PROJECT_ROOT / slug).exists()

    def rename(
        self,
        slug: str,
        new_name: str,
    ) -> Project:
        project = self.get(slug)

        new_name = new_name.strip()

        if not new_name:
            raise ValueError("Project name cannot be empty.")
            
        if new_name.lower() in RESERVED_PROJECT_NAMES:
            raise ValueError("Project name cannot be a reserved word.")

        # Compute the new slug from the new name
        new_slug = Project.create(new_name).slug

        source_folder = self.PROJECT_ROOT / slug
        dest_folder = self.PROJECT_ROOT / new_slug

        # If destination already exists (and is not the same as source), abort
        if self.exists(new_slug) and new_slug != slug:
            raise ValueError(
                f"Destination project '{new_slug}' already exists."
            )

        # If slug unchanged, just update metadata in place
        if new_slug == slug:
            project.name = new_name
            project.updated_at = datetime.now(UTC).isoformat(timespec="seconds")
            project.save(source_folder)
            return project

        try:
            shutil.move(str(source_folder), str(dest_folder))
        except Exception as exc:
            raise RuntimeError(
                f"Failed to rename project directory: {exc}"
            ) from exc

        # Update metadata after successful move
        project.name = new_name
        project.slug = new_slug
        project.updated_at = datetime.now(UTC).isoformat(timespec="seconds")
        project.save(dest_folder)
        return project

    def delete(
        self,
        slug: str,
    ) -> None:
        """
        Delete a project by its slug.

        Args:
            slug (str): The slug of the project to delete

        Raises:
            FileNotFoundError: If the project does not exist
        """
        folder = (
            self.PROJECT_ROOT / slug
        )

        if not folder.exists():

            raise FileNotFoundError(
                slug
            )

        # Ensure we're only deleting within our project root
        if not str(folder.resolve()).startswith(str(self.PROJECT_ROOT.resolve())):
            raise ValueError("Invalid project path - cannot delete outside of project root")

        shutil.rmtree(folder)


project_service = ProjectService()