"""
Tests for the project service.
"""

from __future__ import annotations

import shutil
import pytest
import tempfile
import os

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
        
def cleanup_all_projects() -> None:
    """Remove all projects to avoid conflicts in tests."""
    import glob
    # Remove all project directories except the one we know exists  
    for project_dir in PROJECT_ROOT.iterdir():
        if project_dir.is_dir() and not (project_dir / "project.json").exists():
            continue  # Skip non-project directories
        try:
            shutil.rmtree(project_dir)
        except Exception:
            pass  # Continue even if some cleanup fails


def test_create_project() -> None:

    cleanup()

    project = project_service.create(TEST_PROJECT)

    assert project.name == TEST_PROJECT
    assert project.slug == TEST_SLUG

    cleanup()


def test_project_listing() -> None:

    projects = project_service.list()

    assert isinstance(projects, list)


def test_create_reserved_project_name() -> None:
    """Test that creating a project with a reserved name raises ValueError."""
    
    # Clean up any existing projects first
    cleanup_all_projects()
    
    reserved_names = ["new", "delete", "edit", "settings", "story"]
    
    for name in reserved_names:
        # Test case insensitive
        upper_name = name.upper()
        mixed_case_name = name.capitalize()
        
        # These should all raise ValueError 
        with pytest.raises(ValueError, match="Project name cannot be a reserved word"):
            project_service.create(name)
            
        with pytest.raises(ValueError, match="Project name cannot be a reserved word"):
            project_service.create(upper_name)
            
        with pytest.raises(ValueError, match="Project name cannot be a reserved word"):
            project_service.create(mixed_case_name)
            
        # Test whitespace trimming
        with pytest.raises(ValueError, match="Project name cannot be a reserved word"):
            project_service.create(f"  {name}  ")
        
        # Test that non-reserved names work fine 
        valid_project = project_service.create(f"Valid Project Name {name}")
        assert valid_project.name == f"Valid Project Name {name}"
        assert valid_project.slug == f"valid-project-name-{name}"


def test_create_duplicate_project_name() -> None:
    """Test that creating a duplicate project raises FileExistsError."""
    
    cleanup()
    
    # Create first project
    project_service.create(TEST_PROJECT)
    
    # Try to create another with same name - should raise error 
    try:
        project_service.create(TEST_PROJECT)
        assert False, "Should have raised FileExistsError"
    except FileExistsError:
        pass  # Expected
        
    cleanup()


def test_create_project_whitespace_only_name() -> None:
    """Test creating a project with whitespace-only name raises an error."""
    # Test various whitespace-only inputs
    whitespace_inputs = ["   ", "\t\n\r", " \t \n \r ", ""]

    for whitespace_input in whitespace_inputs:
        with pytest.raises(ValueError, match="cannot be empty"):
            project_service.create(whitespace_input)
            
    # Test that non-whitespace names work fine
    valid_project = project_service.create("Valid Project Name")
    assert valid_project.name == "Valid Project Name"


