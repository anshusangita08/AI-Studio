# Documentation Architecture

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document defines how documentation is organized within the AI Studio repository.

The objective is to ensure documentation remains maintainable, discoverable, and free from unnecessary duplication.

---

# Documentation Hierarchy

Documentation is organized into four categories:

1. Core documentation
2. Living documentation
3. Templates
4. Historical documentation

---

# Core Documentation

Core documentation explains how the project works.

Examples include:

- README.md
- PROJECT.md
- ARCHITECTURE.md
- PROJECT_PHILOSOPHY.md
- PROJECT_CONVENTIONS.md
- FILE_STRUCTURE.md

These documents change infrequently.

---

# Living Documentation

Living documentation changes throughout development.

Examples include:

- PROGRESS.md
- CHANGELOG.md
- ROADMAP.md
- KNOWN_LIMITATIONS.md

These documents should be reviewed regularly.

---

# Development Documentation

Development documentation explains how contributors should work.

Examples include:

- DEVELOPMENT_WORKFLOW.md
- GIT_WORKFLOW.md
- CONTRIBUTING.md
- CODING_STANDARDS.md
- IMPLEMENTATION_PRINCIPLES.md
- TESTING.md
- QUALITY_ASSURANCE.md

---

# Technical Documentation

Technical documentation explains implementation details.

Examples include:

- CONFIGURATION.md
- SECURITY.md
- DEPENDENCIES.md
- ERROR_HANDLING.md
- PERFORMANCE_GUIDELINES.md

---

# Reference Documentation

Reference documentation provides supporting information.

Examples include:

- FAQ.md
- GLOSSARY.md
- DOCUMENTATION_INDEX.md

---

# Templates

Reusable templates should remain generic.

Examples include:

- ISSUE_TEMPLATE.md
- DECISION_LOG_TEMPLATE.md
- MILESTONE_CHECKLIST.md
- PULL_REQUEST_CHECKLIST.md
- DOCUMENTATION_CHECKLIST.md

Templates should never contain project-specific implementation details.

---

# Historical Documentation

Historical documentation belongs under:

```text
docs/old/
```

Historical documentation:

- Preserves project history.
- Should not duplicate current documentation.
- Should not be used as the primary source of truth.

---

# Milestone Documentation

Milestone documents belong under:

```text
docs/milestones/
```

Each milestone should record:

- Objectives
- Completed work
- Testing summary
- Outstanding items
- Completion status

Completed milestones serve as historical implementation records.

---

# Single Source of Truth

Every topic should have one authoritative document.

If multiple documents discuss the same topic:

- Keep detailed information in one document.
- Replace duplication with references.

---

# Maintenance

When documentation changes:

1. Update the authoritative document.
2. Review related documents.
3. Remove obsolete information.
4. Verify cross-references.
5. Commit documentation with the implementation whenever practical.

---

End of Documentation Architecture.