# Services Reference

Version: 1.0

Status: Living Documentation

---

# Purpose

This document describes the service layer used by AI Studio.

Services implement business logic and act as the bridge between the HTTP routes and the filesystem.

---

# Service Layer Responsibilities

Services are responsible for:

- Business logic
- Validation
- Filesystem operations
- Data transformation
- Workflow coordination

Services should not:

- Render HTML
- Handle HTTP requests directly
- Contain presentation logic

---

# Service Architecture

```text
Browser
      │
      ▼
FastAPI Route
      │
      ▼
Service
      │
      ▼
Filesystem
```

---

# Service Design Principles

Every service should:

- Have a single responsibility.
- Be reusable.
- Be independently testable.
- Minimize external dependencies.
- Handle expected errors gracefully.

---

# Typical Services

## Project Service

Responsible for:

- Create project
- Rename project
- Delete project
- Load project
- List projects

---

## Story Service

Responsible for:

- Create story
- Save story
- Load story
- Expand story
- Manage story data

---

## Scene Service

Responsible for:

- Generate scenes
- Save scenes
- Update scenes
- Delete scenes
- Load scenes

---

## AI Service

Responsible for:

- AI requests
- Prompt execution
- Response handling
- Model communication
- Retry handling

---

## Configuration Service

Responsible for:

- Load configuration
- Validate configuration
- Save configuration
- Provide application settings

---

## Workspace Service

Responsible for:

- Directory management
- Project discovery
- Workspace validation
- Runtime storage

---

# Service Communication

Services should communicate through clearly defined interfaces.

Avoid direct dependencies between unrelated services whenever practical.

---

# Error Handling

Services should:

- Validate inputs.
- Raise meaningful exceptions.
- Preserve data integrity.
- Log significant failures.

---

# Testing

Each service should be covered by:

- Unit tests
- Integration tests where appropriate
- Manual verification of user workflows

---

# Best Practices

- Keep methods focused.
- Avoid duplicated logic.
- Reuse existing services.
- Keep filesystem access centralized.
- Preserve architectural boundaries.

---

# Related Documents

- ARCHITECTURE.md
- ARCHITECTURE_PRINCIPLES.md
- IMPLEMENTATION_PRINCIPLES.md
- TESTING.md

---

End of Services Reference.