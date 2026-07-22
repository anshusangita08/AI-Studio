"""
Tests for the project service.
"""

from __future__ import annotations

import shutil
import pytest
import tempfile
import os
from pathlib import Path
import json
import zipfile

from app.services.project_service import (
    ProjectService,
)


TEST_PROJECT = "PyTest Project"
TEST_SLUG = "pytest-project"


def test_create_project(tmp_path) -> None:
    # Create a fresh project service instance with isolated workspace directly in tmp_path
    project_service = ProjectService()
    # Override the PROJECT_ROOT to point to tmp_path/projects for this test run
    project_service.PROJECT_ROOT = Path(tmp_path) / "projects"
    project_service.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    project = project_service.create(TEST_PROJECT)

    assert project.name == TEST_PROJECT
    assert project.slug == TEST_SLUG


def test_project_listing(tmp_path) -> None:
    # Create a fresh project service instance with isolated workspace
    project_service = ProjectService()
    # Override the PROJECT_ROOT to point to tmp_path/projects for this test run
    project_service.PROJECT_ROOT = Path(tmp_path) / "projects"
    project_service.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    projects = project_service.list()

    assert isinstance(projects, list)


def test_create_reserved_project_name(tmp_path) -> None:
    """Test that creating a project with a reserved name raises ValueError."""
    
    # Create.. (same as before)
    project_service = ProjectService()
    project_service.PROJECT_ROOT = Path(tmp_path) / "projects"
    project_service.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    reserved_names = ["new", "delete", "edit", "settings", "story"]
    
    for i, name in enumerate(reserved_names):
        with pytest.raises(ValueError, match="Project name cannot be a reserved word"):
            project_service.create(name)
            
        with pytest.raises(ValueError, match="Project name cannot be a reserved word"):
            project_service.create(name.upper())
            
        with pytest.raises(ValueError, match="Project name cannot be a reserved word"):
            project_service.create(name.capitalize())
            
        # Test whitespace trimming
        with pytest.raises(ValueError, match="Project name cannot be a reserved word"):
            project_service.create(f"  {name}  ")
        
        valid_project = project_service.create(f"Valid Project Name {name}_{i}")
        assert valid_project.name == f"Valid Project Name {name}_{i}"


def test_create_duplicate_project_name(tmp_path) -> None:
    """... (same as before)"""
    project_service = ProjectService()
    project_service.PROJECT_ROOT = Path(tmp_path) / "projects"
    project_service.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    project_service.create("Test Project Unique")
    
    with pytest.raises(FileExistsError):
        project_service.create("Test Project Unique")


def test_create_project_whitespace_only_name(tmp_path) -> None:
    """... (same as before)"""
    project_service = ProjectService()
    project_service.PROJECT_ROOT = Path(tmp_path) / "projects"
    project_service.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    whitespace_inputs = ["   ", "\t\n\r", " \t \n \r ", ""]
    for ws in whitespace_inputs:
        with pytest.raises(ValueError, match="cannot be empty"):
            project_service.create(ws)
    
    valid_project = project_service.create("Valid Project Name")
    assert valid_project.name == "Valid Project Name"


# NEW TESTS FOR EXPORT

def test_export_success(tmp_path) -> None:
    """Create a project and export it."""
    project_service = ProjectService()
    project_service.PROJECT_ROOT = Path(tmp_path) / "projects"
    project_service.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    proj = project_service.create("ExportTest")
    
    # Create a sample file in the story directory to ensure non‑empty content
    story_dir = project_service.PROJECT_ROOT / proj.slug / "story"
    story_dir.mkdir(parents=True, exist_ok=True)
    (story_dir / "story.md").write_text("# Sample Story")

    zip_path = project_service.export_project(proj.slug)
    assert zip_path.exists()
    # Check that the ZIP contains expected files
    with zipfile.ZipFile(zip_path) as zf:
        names = set(zf.namelist())
        assert "project.json" in names
        assert any(n.startswith("story/") for n in names)
        assert "story/story.md" in names


def test_export_manifest_and_exclusions(tmp_path) -> None:
    """Check that manifest.json exists and excluded folders are not included."""
    project_service = ProjectService()
    project_type = Path(tmp_path) / "projects"
    project_service.PROJECT_ROOT = project_type
    project_type.mkdir(parents=True, exist_ok=True)

    # create project with some files in different dirs
    proj = project_service.create("ManifestTest")
    # (proj.slug).mkdir()  # placeholder? actually need to use folder path
    # Create dummy files
    folder = project_service.PROJECT_ROOT / proj.slug
    for d in ["story", "prompts", "images", "audio", "video"]:
        (folder / d).mkdir(parents=True, exist_ok=True)
        (folder / d / f"{d}.txt").write_text("test")
    # create excluded dirs
    for d in ["cache", "temp", *["exports"]]:
        (folder / d).mkdir(parents=True, exist_ok=True)

    zip_path = project_service.export_project(proj.slug)
    with zipfile.ZipFile(zip_path) as zf:
        names = set(zf.namelist())
        assert "manifest.json" in names
        # excluded dirs should not appear
        for d in ["cache", "temp", "exports"]:
            assert all(not n.startswith(d + "/") for n in names)


def test_export_missing_project(tmp_path) -> None:
    """The export function should raise FileNotFoundError when missing."""
    project_service = ProjectService()
    project_service.PROJECT_ROOT = Path(tmp_path) / "projects"
    project_service.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    with pytest.raises(FileNotFoundError):
        project_service.export_project("nonexistent")


# NEW TEST: verify asset directories are created on project creation
def test_asset_folders_created(tmp_path) -> None:
    """Ensure that assets/, assets/images/ etc. are created automatically."""
    project_service = ProjectService()
    project_service.PROJECT_ROOT = Path(tmp_path) / "projects"
    project_service.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    proj = project_service.create("AssetTest")
    asset_root = project_service.PROJECT_ROOT / proj.slug / "assets"

    assert asset_root.exists()
    assert (asset_root / "images").exists()
    assert (asset_root / "audio").exists()
    assert (asset_root / "video").exists()
