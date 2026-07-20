# Release Process

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document defines the release process for AI Studio.

The objective is to ensure every release is stable, tested, documented, and reproducible.

---

# Release Workflow

A release follows this sequence:

1. Complete milestone.
2. Complete testing.
3. Perform manual verification.
4. Update documentation.
5. Update CHANGELOG.md.
6. Commit final changes.
7. Create release tag.
8. Publish release.

---

# Pre-Release Checklist

Before every release verify:

- All planned work completed.
- No known blocking issues.
- Automated tests pass.
- Manual verification completed.
- Documentation updated.
- Changelog updated.
- Repository builds successfully.

---

# Documentation Checklist

Update when applicable:

- PROGRESS.md
- Current milestone document
- CHANGELOG.md

Architecture and project documentation should only be updated if they have changed.

---

# Versioning

Releases should use semantic versioning.

```text
MAJOR.MINOR.PATCH
```

Example:

```text
1.0.0
1.1.0
1.1.1
```

---

# Release Tag

Recommended format:

```text
v1.0.0
```

---

# Release Notes

Each release should include:

- Summary
- New features
- Improvements
- Bug fixes
- Breaking changes
- Known limitations

---

# Post-Release

After a successful release:

- Verify repository state.
- Update current development milestone.
- Begin the next milestone.
- Update PROGRESS.md.

---

# Emergency Fixes

Critical fixes should:

- Address one issue.
- Be fully tested.
- Update CHANGELOG.md.
- Be released as a patch version.

---

# Principles

- Release only tested code.
- Keep releases reproducible.
- Keep release notes concise.
- Every release must be documented.

---

End of Release Process.