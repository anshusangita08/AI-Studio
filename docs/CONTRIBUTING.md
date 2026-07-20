# Contributing Guide

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document defines the contribution process for AI Studio.

All contributors should follow these guidelines to maintain a consistent, stable, and maintainable codebase.

---

# Before You Start

Before making changes:

- Read `REPOSITORY_RULES.md`.
- Read `PROJECT.md`.
- Read `ARCHITECTURE.md`.
- Read `CODING_STANDARDS.md`.
- Read `TESTING.md`.
- Review `PROGRESS.md`.

---

# Development Workflow

Every contribution should follow this sequence:

1. Understand the requirement.
2. Review the existing implementation.
3. Create a small implementation plan.
4. Modify only the required files.
5. Test the implementation.
6. Perform manual verification where applicable.
7. Update documentation.
8. Commit the changes.

---

# Pull Request Guidelines

Each pull request should:

- Address a single objective.
- Keep changes focused.
- Include appropriate tests.
- Avoid unrelated modifications.
- Preserve existing architecture.

---

# Commit Guidelines

Commits should:

- Be small and focused.
- Use clear commit messages.
- Represent a single logical change.

Examples:

```text
feat: add story export
fix: resolve project rename bug
docs: update architecture
refactor: simplify story service
test: add persistence tests
```

---

# Documentation

When required, update:

- PROGRESS.md
- Current milestone document
- CHANGELOG.md

Do not duplicate documentation across multiple files.

---

# Code Quality

All contributions should:

- Follow project coding standards.
- Preserve architecture.
- Reuse existing components.
- Avoid unnecessary dependencies.
- Avoid unnecessary refactoring.

---

# Testing Requirements

Before submitting changes:

- Automated tests pass.
- Manual verification completed where applicable.
- Existing functionality remains operational.

---

# Review Checklist

Before merging:

- Implementation complete.
- Tests completed.
- Documentation updated.
- No unrelated changes included.
- Repository remains buildable.

---

End of Contributing Guide.