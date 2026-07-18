"""
Tests for the project service.
"""

from __future__ import annotations

import shutil
import pytest
import tempfile
import os
from pathlib import Path

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
    
    # Create a fresh project service instance with isolated workspace
    project_service = ProjectService()
    # Override the PROJECT_ROOT to point to tmp_path/projects for this test run
    project_service.PROJECT_ROOT = Path(tmp_path) / "projects"
    project_service.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    reserved_names = ["new", "delete", "edit", "settings", "story"]
    
    # Test each reserved name with a different suffix to prevent conflicts in the same test session
    for i, name in enumerate(reserved_names):
        # These should all raise ValueError 
        with pytest.raises(ValueError, match="Project name cannot be a reserved word"):
            project_service.create(name)
            
        with pytest.raises(ValueError, match="Project name cannot be a reserved word"):
            project_service.create(name.upper())
            
        with pytest.raises(ValueError, match="Project name cannot be a reserved word"):
            project_service.create(name.capitalize())
            
        # Test whitespace trimming
        with pytest.raises(ValueError, match="Project name cannot be a reserved word"):
            project_service.create(f"  {name}  ")
        
        # Test that non-reserved names work fine - using unique suffixes to prevent conflicts within same test session
        valid_project = project_service.create(f"Valid Project Name {name}_{i}")
        assert valid_project.name == f"Valid Project Name {name}_{i}"


def test_create_duplicate_project_name(tmp_path) -> None:
    """Test that creating a duplicate project raises FileExistsError."""
    
    # Create a fresh project service instance with isolated workspace
    project_service = ProjectService()
    # Override the PROJECT_ROOT to point to tmp_path/projects for this test run
    project_service.PROJECT_ROOT = Path(tmp_path) / "projects"
    project_service.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    # Create first project - using unique name to prevent conflicts within same test session
    project_service.create("Test Project Unique")
    
    # Try to create another with same name (but different slug for testing purposes) - should raise error 
    try:
        project_service.create("Test Project Unique")  # This will have the same slug, so it should fail
        assert False, "Should have raised FileExistsError"
    except FileExistsError:
        pass  # Expected


def test_create_project_whitespace_only_name(tmp_path) -> None:
    """Test creating a project with whitespace-only name raises an error."""
    # Create a fresh project service instance with isolated workspace
    project_service = ProjectService()
    # Override the PROJECT_ROOT to point to tmp_path/projects for this test run
    project_service.PROJECT_ROOT = Path(tmp_path) / "projects"
    project_service.PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    # Test various whitespace-only inputs
    whitespace_inputs = ["   ", "\t\n\r", " \t \n \r ", ""]

    for whitespace_input in whitespace_inputs:
        with pytest.raises(ValueError, match="cannot be empty"):
            project_service.create(whitespace_input)
            
    # Test that non-whitespace names work fine
    valid_project = project_service.create("Valid Project Name")
    assert valid_project.name == "Valid Project Name"
