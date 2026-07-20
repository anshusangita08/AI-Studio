# REPOSITORY_RULES.md

Version: 1.0
Status: Permanent Repository Policy
Last Updated: 2026-07-20

---

# Purpose

This document defines the permanent rules governing the AI Studio repository.

It is the highest-level project document and serves as the repository constitution.

Its purpose is to ensure that the repository remains organized, maintainable, and predictable throughout the lifetime of the project.

These rules apply to all contributors, including human developers and AI assistants.

This document should not be modified unless the repository standards themselves change.

---

# Repository Philosophy

The repository must remain:

* Simple
* Predictable
* Modular
* Local-first
* Easy to navigate
* Easy to maintain
* Production quality

The repository structure must always be preferred over convenience.

---

# Single Source of Truth

Every topic within the repository must have exactly one authoritative location.

Duplicate documentation is not permitted.

Duplicate implementation guidance is not permitted.

Conflicting documentation is not permitted.

Whenever information changes, it must be updated only in its designated document.

---

# Repository Structure

The project root contains only repository assets and application entry points.

Typical project layout:

```text
AI-Studio/
│
├── app/
├── config/
├── docs/
├── static/
├── tests/
├── workspace/
│
├── launcher.py
├── run.bat
├── requirements.txt
├── pyproject.toml
├── README.md
├── LICENSE
├── .gitignore
│
└── REPOSITORY_RULES.md
```

No additional documentation files should exist in the project root.

---

# Documentation Policy

All project documentation must exist inside the **docs/** directory.

No Markdown documentation files are permitted outside **docs/** except:

* README.md
* LICENSE (if Markdown)
* REPOSITORY_RULES.md

All new documentation must be placed within the documentation structure.

---

# Documentation Structure

```text
docs/
│
├── README.md
├── PROJECT.md
├── ARCHITECTURE.md
├── PROGRESS.md
│
└── milestones/
```

This structure is permanent unless explicitly changed.

---

# Documentation Responsibilities

## README.md

Documentation index.

Contains:

* Documentation overview
* Repository navigation
* Links to all documentation

It must not contain project status.

---

## PROJECT.md

Defines the project itself.

Contains:

* Vision
* Goals
* Features
* Technology stack
* Repository overview
* Development workflow
* AI development workflow

It must not contain milestone progress.

---

## ARCHITECTURE.md

Defines the technical architecture.

Contains:

* Folder responsibilities
* Request flow
* Service relationships
* Storage
* Pipelines
* Design principles
* Architectural constraints

It must never contain project status.

---

## PROGRESS.md

The only living project status document.

Contains:

* Current milestone
* Current objective
* Completed milestones
* Current work
* Working files
* Known issues
* Test status
* Next step

Every implementation updates this document.

No other document may duplicate project status.

---

## milestones/

Each milestone has exactly one document.

Milestone documents contain:

* Requirements
* Acceptance criteria
* Implementation summary
* Files changed
* Tests
* Completion notes

Once a milestone is marked complete it becomes historical documentation.

Completed milestone documents should not be modified unless correcting factual inaccuracies.

---

# Documentation Rules

Every document has one responsibility.

A document must never duplicate another document.

If information belongs somewhere else, move it rather than copy it.

Documentation should describe the current implementation.

Documentation must never speculate about future implementations.

Unknown information should be explicitly identified rather than invented.

When implementation changes:

* Update only the affected documentation.
* Do not perform unrelated documentation edits.
* Keep documentation synchronized with the source code.

If documentation conflicts with the source code, the source code is considered authoritative until the documentation is corrected.

---

# Development Principles

Development must remain incremental.

Large refactors are discouraged unless explicitly approved.

Existing architecture should be preserved whenever practical.

Backward compatibility should be maintained whenever possible.

Working code should not be rewritten solely for stylistic reasons.

Every change should have a clear purpose.

---

# AI Development Workflow

AI assistance is a core part of this project's development process.

Current development tools include:

* ChatGPT
* Aider
* Continue
* Cline
* LM Studio
* VS Code

These tools have different responsibilities and should be used accordingly.

High-level planning, architecture, reviews, and debugging should occur before implementation.

Large implementations should be performed incrementally.

Small isolated edits may be completed using lightweight tools.

All AI-generated code must be reviewed before being accepted.

---

# Testing Policy

Implementation is not considered complete until testing has been performed.

Where applicable:

* Existing tests should continue to pass.
* New functionality should include appropriate tests.
* Manual verification should be performed for user-facing functionality.

Testing should occur before commits.

---

# Git Policy

The repository follows a stable development workflow.

Main principles:

* Develop on development branches.
* Keep the main branch stable.
* Commit only after successful testing.
* Keep commits focused.
* Avoid unrelated changes in the same commit.

---

# Repository Cleanliness

The repository should remain uncluttered.

Avoid:

* Duplicate documentation
* Temporary files
* Personal notes
* Experimental documents
* Obsolete documentation
* Generated runtime artifacts committed to source control

Git history should preserve project evolution rather than duplicate files within the repository.

---

# Permanent Rules

The following rules are non-negotiable unless explicitly changed by the repository owner.

* Documentation exists only inside **docs/**.
* Every topic has one authoritative document.
* Every milestone has one milestone document.
* PROGRESS.md is the single source of truth for project status.
* Architecture is documented only in ARCHITECTURE.md.
* Project definition is documented only in PROJECT.md.
* Documentation follows the implementation.
* Source code is authoritative.
* Repository structure takes priority over convenience.
* Keep the repository clean, consistent, and maintainable.

---

End of Repository Rules.
