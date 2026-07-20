# Naming Conventions

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document defines the naming conventions used throughout the AI Studio project.

Consistent naming improves readability, maintainability, and discoverability.

---

# General Principles

Names should be:

- Descriptive
- Consistent
- Predictable
- Concise
- Easy to search

Avoid abbreviations unless they are widely understood.

---

# Files

Use:

- Lowercase
- Underscores between words

Examples:

```text
project_service.py
story_service.py
image_generator.py
```

Avoid:

```text
ProjectService.py
Story-Service.py
file1.py
```

---

# Directories

Directory names should:

- Be lowercase
- Use underscores only when necessary
- Clearly describe their purpose

Examples:

```text
services/
templates/
static/
workspace/
tests/
```

---

# Python Modules

Module names should:

- Be lowercase
- Use underscores where appropriate
- Represent a single responsibility

Example:

```text
scene_service.py
```

---

# Classes

Use:

- PascalCase

Examples:

```python
ProjectService
StoryPlanner
SceneGenerator
```

---

# Functions

Use:

- snake_case

Examples:

```python
create_project()
generate_story()
save_scene()
```

Function names should begin with a verb whenever practical.

---

# Variables

Use:

- snake_case

Examples:

```python
project_name
story_data
scene_count
output_directory
```

Avoid overly short variable names except for simple loop variables.

---

# Constants

Use:

- UPPER_CASE

Examples:

```python
DEFAULT_PORT
MAX_RETRIES
DEFAULT_TIMEOUT
```

---

# Boolean Variables

Boolean names should clearly indicate a true/false value.

Examples:

```python
is_valid
has_story
should_retry
is_complete
```

---

# HTML Templates

Template names should describe the page or component.

Examples:

```text
index.html
story_planner.html
project_list.html
```

---

# CSS

Class names should be descriptive.

Example:

```text
project-card
story-panel
navigation-menu
```

Avoid presentation-specific names where possible.

---

# API Routes

Routes should:

- Use lowercase
- Use nouns
- Remain predictable

Examples:

```text
/projects
/stories
/scenes
```

---

# Documentation

Documentation filenames should use uppercase with underscores for consistency.

Examples:

```text
README.md
PROJECT.md
ARCHITECTURE.md
TESTING.md
```

---

# Git Branches

Recommended names:

```text
main
develop
feature/story-planner
bugfix/project-delete
docs/update-guides
```

---

# Commit Messages

Follow the conventions defined in:

`docs/GIT_WORKFLOW.md`

---

# Principles

Naming should prioritize:

- Readability
- Consistency
- Maintainability
- Searchability

When in doubt, choose the clearer name.

---

End of Naming Conventions.