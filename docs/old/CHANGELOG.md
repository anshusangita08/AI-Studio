Milestone 008.5

Completed
- Project creation
- Project listing
- Project opening
- Project deletion
- Project rename
- Directory rename on disk
- Redirect to new slug after rename
- Reserved name validation
- Duplicate name validation
- Rename unit tests (30 passing)
Notes
- All project CRUD operations now fully implemented and tested.
Milestone 008.4

Completed
- Fixed Story Planner rendering regressions.
- Fixed Story generation workflow.
- Fixed Scene generation workflow.
- Fixed Scene persistence after refresh.
- Restored Project delete workflow.
- Improved Story context loading.
- Added/updated tests for Story services.

Notes
- Delete Project was verified to work correctly.
- An apparent delete regression was traced to the VS Code embedded browser suppressing native confirm() dialogs. No application code change was required for deletion.
- Story Planner fixes documented in PROJECT.md
- Scene persistence fix documented in PROJECT.md  
- Project delete verification documented in PROJECT.md

## Refactor: ProjectService test isolation

- This repository uses a module‑level `ProjectService` instance (`project_service = ProjectService()`) for production compatibility.
- The refactor preserves that singleton while allowing tests to instantiate isolated `ProjectService(root=tmp_path / "projects")` instances with configurable project roots. Tests now operate entirely inside temporary directories, eliminating filesystem side effects without changing production behavior.
- No filesystem side‑effects in `workspace/projects` during pytest runs.
- Internal test infrastructure improvement only; no user‑visible changes.


