import os
from pathlib import Path
import shutil
import pytest

from app.services.project_service import ProjectService, Project

# Helper to create a project with a dummy file inside story directory

def _create_project_with_file(service: ProjectService, name: str, filename: str, content: str):
    proj = service.create(name)
    (service.PROJECT_ROOT / proj.slug / "story" / filename).write_text(content)
    return proj


def test_rename_success(tmp_path):
    # Setup isolated project root
    service = ProjectService()
    service.PROJECT_ROOT = tmp_path / "projects"
    service.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    # Create a project and add a file
    proj = _create_project_with_file(service, "Test Project", "test.txt", "content")

    new_name = "New Name"
    renamed_proj = service.rename(proj.slug, new_name)

    assert renamed_proj.name == new_name
    # slug should change based on new name
    expected_slug = Project.create(new_name).slug
    assert renamed_proj.slug == expected_slug

    # Original folder should no longer exist
    assert not (service.PROJECT_ROOT / proj.slug).exists()
    # Destination folder exists
    dest_folder = service.PROJECT_ROOT / renamed_proj.slug
    assert dest_folder.exists()

    # File content preserved
    assert (dest_folder / "story" / "test.txt").read_text() == "content"


def test_rename_duplicate_destination(tmp_path):
    service = ProjectService()
    service.PROJECT_ROOT = tmp_path / "projects"
    service.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    p1 = service.create("Alpha")
    p2 = service.create("Beta")  # slug 'beta'

    with pytest.raises(ValueError, match="Destination project 'beta' already exists."):
        service.rename(p1.slug, "Beta")  # new_name Beta -> slug 'beta'


def test_rename_fs_failure(tmp_path, monkeypatch):
    service = ProjectService()
    service.PROJECT_ROOT = tmp_path / "projects"
    service.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    proj = _create_project_with_file(service, "Fail", "file.txt", "data")

    # Simulate failure of shutil.move
    def fake_move(src, dst):  # pragma: no cover
        raise OSError("simulated failure")
    monkeypatch.setattr(shutil, 'move', fake_move)

    with pytest.raises(RuntimeError, match="Failed to rename project directory"):
        service.rename(proj.slug, "NewName")

    # Original folder should still exist
    assert (service.PROJECT_ROOT / proj.slug).exists()
    # Destination folder should not exist
    new_slug = Project.create("NewName" ).slug
    assert not (service.PROJECT_ROOT / new_slug).exists()
