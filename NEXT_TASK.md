# Current Milestone
008.3b – Story Planner UX Refresh

# Current Objective
Refactor the Story Planner UI into smaller reusable components before implementing new features.

# Current Status
In Progress

# Files To Modify
app/ui/routes_story.py
app/ui/templates/projects/story.html

# Tests To Run
python -m pytest tests/ -v

# Definition of Done
- Story page split into smaller reusable templates.
- Story, Expanded Story and Scenes each have independent save workflows.
- Layout is responsive.
- Existing functionality preserved.
- Tests pass.

# After Completion
Update PROJECT_STATE.md and begin the next UX enhancement.
