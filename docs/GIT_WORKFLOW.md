# Git Workflow

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document defines the Git workflow used during AI Studio development.

The workflow emphasizes stability, traceability, and incremental development.

---

# Branch Strategy

## main

Purpose:

- Stable production-ready code.
- Every commit should be deployable.
- Protected from direct experimental work.

---

## develop

Purpose:

- Active development.
- Integration of completed milestone work.
- Default branch for feature implementation.

---

# Development Workflow

For every feature:

1. Switch to `develop`.
2. Implement the feature.
3. Test the implementation.
4. Update documentation.
5. Commit changes.
6. Merge into `main` after verification.

---

# Commit Guidelines

Each commit should:

- Represent one logical change.
- Build successfully.
- Keep tests passing.
- Include related documentation updates.

Avoid combining unrelated work into a single commit.

---

# Commit Message Format

Recommended format:

```text
type: short description
```

Examples:

```text
feat: add story planner persistence
fix: resolve project deletion issue
docs: update milestone documentation
test: improve story service coverage
refactor: simplify project service
```

---

# Merge Rules

Before merging:

- Automated tests pass.
- Manual verification completed.
- Documentation updated.
- No known blocking issues.

---

# Conflict Resolution

When merge conflicts occur:

- Resolve conflicts carefully.
- Preserve intended functionality.
- Re-run affected tests.
- Verify application behavior.

---

# Tags

Stable releases should be tagged.

Recommended format:

```text
v1.0.0
```

---

# History

Keep commit history:

- Meaningful
- Readable
- Traceable

Avoid unnecessary commits that only contain temporary work.

---

# Repository Hygiene

Do not commit:

- Temporary files
- Cache files
- Generated artifacts
- Local configuration overrides
- Virtual environments

---

# Recovery

If a commit introduces regressions:

1. Identify the cause.
2. Fix the issue or revert the commit.
3. Re-run tests.
4. Verify application stability.
5. Document the resolution if necessary.

---

# Best Practices

- Commit frequently.
- Keep commits focused.
- Test before committing.
- Merge only stable code.
- Keep `main` production-ready.
- Maintain documentation alongside code.

---

End of Git Workflow.