# Data Model

Version: 1.0

Status: Living Documentation

---

# Purpose

This document describes the logical data model used by AI Studio.

The application stores project information using the local filesystem rather than a database.

---

# Design Principles

The data model should be:

- Human readable
- Portable
- Versionable
- Easy to back up
- Independent of database engines

---

# Storage Model

```text
Workspace
    │
    ├── Project
    │      │
    │      ├── Story
    │      ├── Scenes
    │      ├── Assets
    │      └── Metadata
    │
    └── Additional Projects
```

---

# Project

A project is the highest-level container.

A project may contain:

- Story
- Scene definitions
- Generated assets
- Configuration
- Metadata

Each project should remain self-contained.

---

# Story

A story represents the primary narrative.

Typical information includes:

- Title
- Description
- Genre
- Style
- Expanded story
- Prompt information

Only one active story should exist per project unless future requirements specify otherwise.

---

# Scene

Scenes divide a story into smaller units.

Each scene may contain:

- Scene number
- Title
- Description
- Dialogue
- Prompt
- Notes
- Generation status

Scenes should be independently editable.

---

# Assets

Assets may include:

- Images
- Audio
- Video
- Generated files
- Intermediate outputs

Assets should remain associated with the owning project.

---

# Metadata

Metadata describes project state.

Typical metadata includes:

- Creation date
- Last modified
- Application version
- Project version
- Generation status

---

# Configuration

Project-specific configuration may include:

- AI model selection
- Generation settings
- Export settings
- User preferences

Application-wide configuration should remain separate from project data.

---

# Persistence

The application persists data using the local filesystem.

Persistence should:

- Preserve user work.
- Prevent unnecessary writes.
- Recover gracefully from failures.

---

# Data Integrity

The application should:

- Validate required fields.
- Prevent invalid state.
- Handle partial failures safely.
- Preserve existing data whenever practical.

---

# Future Expansion

The data model should support future additions without requiring major structural changes.

Possible future additions include:

- Characters
- Locations
- Timelines
- Voice profiles
- Animation settings
- Export presets

---

# Related Documents

- FILE_STRUCTURE.md
- ARCHITECTURE.md
- CONFIGURATION.md
- SERVICES.md

---

End of Data Model.