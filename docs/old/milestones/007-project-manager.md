# Milestone 007: Project Manager

## Overview
Project management capabilities including creation, renaming, deletion, and validation.

## Details

### Responsibilities
- Create project
- Rename project
- Delete project
- Validate names
- Reserved names
- Duplicate checking
- Project listing

## Includes
- ✓ Create Project
- ✓ Rename Project
- ✓ Delete Project
- ✓ Reserved names
- ✓ Duplicate validation
- ✓ Empty validation
- ✓ Friendly validation
- ✓ Tests
- ✓ Manual verification

## Status: Completed

**Note:** The repository uses a module‑level `ProjectService` instance (`project_service = ProjectService()`) for production compatibility.  The refactor preserves that singleton while allowing tests to instantiate isolated `ProjectService(root=tmp_path / "projects")` instances with configurable project roots.  Tests now operate entirely inside temporary directories, eliminating filesystem side effects without changing production behavior.
