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
