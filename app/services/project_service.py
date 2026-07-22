"""
Project management service.
"""

from __future__ import annotations

import json
import shutil
from datetime import UTC, datetime
from pathlib import Path
import os

from app.models.project import Project
from app.services.story_service import StoryService
from app.services.prompt_service import PromptService
from app.services.export_service import ExportService
from app.services.render_service import RenderService


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

# New asset sub‑structure to be created automatically
ASSET_SUBSTRUCTURE = (
    "assets",
    "assets/images",
    "assets/audio",
    "assets/video",
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

        # Instantiate feature services for pipeline status checks
        self.story_service = StoryService(projects_dir=str(self.PROJECT_ROOT))
        self.prompt_service = PromptService(projects_dir=str(self.PROJECT_ROOT))

        # Export service
        self.export_service = ExportService(self.PROJECT_ROOT)

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

        # Create the original project structure
        for directory in PROJECT_STRUCTURE:
            (folder / directory).mkdir(parents=True, exist_ok=True)

        # ---- NEW: create asset sub‑structure ---------------------------------
        for directory in ASSET_SUBSTRUCTURE:
            (folder / directory).mkdir(parents=True, exist_ok=True)
        # ---------------------------------------------------------------------

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

    def get_pipeline_status(self, slug: str) -> dict:
        """
        Compute the current pipeline status for a given project.

        Returns a dictionary with keys:
          - story_complete (bool)
          - scenes_complete (bool)
          - prompts_complete (bool)
          - overall_status (str): "Not Started", "In Progress", or "Completed"
        """
        # Ensure project exists
        if not self.exists(slug):
            raise FileNotFoundError(f"Project '{slug}' does not exist")

        story_complete = self.story_service.is_story_complete(slug)
        scenes_complete = self.story_service.are_scenes_complete(slug)
        prompts_complete = self.prompt_service.are_prompts_complete(slug)

        # Determine overall status
        if not any([story_complete, scenes_complete, prompts_complete]):
            overall_status = "Not Started"
        elif all([story_complete, scenes_complete, prompts_complete]):
            overall_status = "Completed"
        else:
            overall_status = "In Progress"

        return {
            "story_complete": story_complete,
            "scenes_complete": scenes_complete,
            "prompts_complete": prompts_complete,
            "overall_status": overall_status,
        }

    def export_project(self, slug: str) -> Path:
        """
        Orchestrate export of a project.
        Returns the path to the created ZIP file.
        """
        # Re‑create ExportService with the current root so that tests using
        # an overridden PROJECT_ROOT work correctly.
        export_service = ExportService(self.PROJECT_ROOT)
        pipeline_status = self.get_pipeline_status(slug)
        return export_service.create_export(slug, pipeline_status)

    def render_project(self, slug: str) -> dict:
        """
        Orchestrate rendering of a project.

        Returns the metadata written by RenderService.
        """
        if not self.exists(slug):
            raise FileNotFoundError(f"Project '{slug}' does not exist")

        project_path = self.PROJECT_ROOT / slug
        render_service = RenderService(project_path)
        return render_service.render()

project_service = ProjectService()
