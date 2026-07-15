"""
Basic tests for ProjectService.
"""

from __future__ import annotations

from app.services.project_service import project_service


def test_create_project() -> None:
    project = project_service.create("PyTest Project")

    assert project.name == "PyTest Project"
    assert project.slug == "pytest-project"


def test_project_listing() -> None:
    projects = project_service.list()

    assert isinstance(projects, list)