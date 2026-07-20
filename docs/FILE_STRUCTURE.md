# Repository Structure

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document describes the directory structure of the AI Studio repository and the responsibility of each top-level directory.

---

# Repository Layout

```text
AI-Studio/
│
├── app/
├── config/
├── docs/
├── tests/
├── workspace/
│
├── launcher.py
├── requirements.txt
├── README.md
└── REPOSITORY_RULES.md
```

---

# Directories

## app/

Contains the application source code.

Typical contents include:

- Routes
- Services
- Templates
- Static assets
- Utilities
- Models
- Configuration helpers

---

## config/

Contains project configuration files.

Examples:

- Default configuration
- Runtime configuration
- Environment configuration

---

## docs/

Contains all project documentation.

This includes:

- Project documentation
- Architecture
- Progress tracking
- Standards
- Milestones
- Historical documentation

---

## tests/

Contains automated tests.

Typical contents include:

- Unit tests
- Integration tests
- Test fixtures
- Mock data

---

## workspace/

Contains runtime-generated application data.

Examples include:

- Projects
- Stories
- Scenes
- Images
- Audio
- Video
- Temporary files

This directory is not part of the application source code.

---

# Root Files

## README.md

Repository entry point.

---

## REPOSITORY_RULES.md

Repository-wide rules and standards.

---

## launcher.py

Application launcher.

---

## requirements.txt

Python dependency list.

---

# Design Principles

The repository follows these principles:

- Clear separation of responsibilities.
- One purpose per directory.
- Documentation separated from source code.
- Runtime data separated from application code.
- Tests separated from implementation.

---

# Adding New Directories

Before creating a new top-level directory:

- Verify that an existing directory cannot be reused.
- Ensure the directory has a single responsibility.
- Update this document if the repository structure changes.

---

End of Repository Structure.