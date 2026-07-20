# Project Conventions

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document defines the project-wide conventions used throughout AI Studio.

These conventions ensure consistency across implementation, documentation, testing, and repository management.

---

# General Principles

The project should remain:

- Consistent
- Predictable
- Readable
- Maintainable
- Well documented

---

# Architecture

The existing architecture should be preserved whenever practical.

Changes that significantly alter project structure should be documented before implementation.

---

# Source of Truth

Each topic should have one authoritative location.

Avoid duplicating documentation or implementation logic.

Examples:

- Progress → `docs/PROGRESS.md`
- Architecture → `docs/ARCHITECTURE.md`
- Changes → `docs/CHANGELOG.md`

---

# Documentation

Documentation should be updated whenever:

- Features change
- Architecture changes
- Configuration changes
- Development workflow changes

Documentation is considered part of implementation.

---

# Testing

Every completed feature should be verified through appropriate testing.

Testing should include:

- Unit testing
- Manual verification
- Regression testing where applicable

---

# Git

Development should occur on:

```text
develop
```

Stable code should reside on:

```text
main
```

Commits should represent one logical change.

---

# Code Organization

Source code should remain organized by responsibility.

Examples include:

- Routes
- Services
- Templates
- Static assets
- Utilities

Avoid mixing responsibilities.

---

# Naming

Follow the naming standards defined in:

`docs/NAMING_CONVENTIONS.md`

---

# Dependencies

Before adding a dependency:

- Verify necessity.
- Review maintenance status.
- Review licensing.
- Document significant additions.

---

# Error Handling

Errors should:

- Be handled gracefully.
- Produce useful diagnostics.
- Preserve application stability.
- Avoid exposing internal details.

---

# Performance

Optimize only after identifying measurable bottlenecks.

Correctness should always take priority over optimization.

---

# Documentation Style

Follow the standards defined in:

`docs/STYLE_GUIDE.md`

---

# Continuous Improvement

Improve the project through:

- Better code
- Better tests
- Better documentation
- Reduced technical debt
- Incremental refactoring

---

# Review Checklist

Before completing work, verify:

- Architecture preserved
- Tests passing
- Documentation updated
- No unnecessary files added
- Repository remains stable

---

End of Project Conventions.