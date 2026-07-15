"""
Tests for the project service.
"""

from __future__ import annotations

import shutil

from app.services.project_service import (
    PROJECT_ROOT,
    project_service,
)


TEST_PROJECT = "PyTest Project"
TEST_SLUG = "pytest-project"


def cleanup() -> None:
    folder = PROJECT_ROOT / TEST_SLUG

    if folder.exists():
        shutil.rmtree(folder)


def test_create_project() -> None:

    cleanup()

    project = project_service.create(TEST_PROJECT)

    assert project.name == TEST_PROJECT
    assert project.slug == TEST_SLUG

    cleanup()


def test_project_listing() -> None:

    projects = project_service.list()

    assert isinstance(projects, list)