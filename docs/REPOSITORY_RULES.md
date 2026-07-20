# Repository Rules

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document defines the repository-wide rules that apply to all development within AI Studio.

These rules are intended to preserve consistency, maintainability, and long-term stability.

---

# Core Principles

Development should prioritize:

- Correctness
- Stability
- Simplicity
- Maintainability
- Testability
- Documentation

---

# Architecture

- Preserve the existing architecture whenever practical.
- Avoid unnecessary redesign.
- Document significant architectural changes.
- Prefer extending existing components over introducing new ones.

---

# Source Code

Source code should:

- Follow project coding standards.
- Have a single responsibility.
- Avoid duplicated logic.
- Remain modular and readable.

---

# Documentation

Documentation is part of implementation.

Whenever applicable, update:

- `docs/PROGRESS.md`
- `docs/CHANGELOG.md`
- Current milestone documentation
- Architecture documentation
- Other affected documents

---

# Testing

Before considering work complete:

- Unit tests should pass.
- Manual verification should be completed.
- Regression testing should be performed where appropriate.

---

# Repository Structure

- Keep source code separate from runtime data.
- Keep documentation under `docs/`.
- Keep tests under `tests/`.
- Keep generated content out of the repository unless intentionally tracked.

---

# Git Rules

- Develop on `develop`.
- Merge stable work into `main`.
- Keep commits focused.
- Use meaningful commit messages.

---

# Dependencies

Before adding a dependency:

- Verify necessity.
- Review licensing.
- Review maintenance status.
- Document significant additions.

---

# Error Handling

Applications should:

- Fail safely.
- Handle expected errors.
- Protect user data.
- Produce meaningful diagnostics.

---

# Documentation Rules

- Maintain one source of truth per topic.
- Avoid duplicated documentation.
- Archive obsolete documentation under `docs/old/`.
- Keep documentation synchronized with implementation.

---

# Code Review

Before merging:

- Verify requirements.
- Verify architecture.
- Verify testing.
- Verify documentation.
- Verify repository cleanliness.

---

# Continuous Improvement

Improve the repository through:

- Incremental refactoring
- Better testing
- Better documentation
- Reduced technical debt
- Performance improvements

---

# Completion Criteria

A change is considered complete only when:

- Implementation is finished.
- Testing is complete.
- Documentation is updated.
- Review is complete.
- Repository remains stable.

---

End of Repository Rules.