# Documentation Policy

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document defines the documentation policy for AI Studio.

Documentation is a required deliverable for every significant change to the project.

---

# Policy

Every change to the project should be evaluated to determine whether documentation requires updating.

Documentation should never intentionally fall behind implementation.

---

# Required Updates

Documentation must be reviewed when:

- Adding a feature
- Fixing a bug
- Refactoring code
- Changing architecture
- Updating dependencies
- Changing configuration
- Modifying development workflow
- Completing a milestone
- Creating a release

---

# Source of Truth

Each topic should have exactly one authoritative document.

If information already exists elsewhere:

- Update the authoritative document.
- Avoid creating duplicate content.
- Replace duplicated information with references where appropriate.

---

# Documentation Standards

Documentation should be:

- Accurate
- Clear
- Concise
- Consistent
- Maintainable

Follow the conventions described in:

- `docs/STYLE_GUIDE.md`
- `docs/DOCUMENTATION_MAINTENANCE.md`

---

# Required Reviews

Before completing work, verify:

- Documentation matches implementation.
- Cross-references remain valid.
- Repository paths are correct.
- Obsolete information has been removed.

---

# Historical Information

Completed milestone records and retired documentation should be archived under:

```text
docs/old/
```

Historical documents should not be used as the primary source of truth.

---

# Responsibility

Every contributor is responsible for maintaining documentation related to their changes.

Documentation updates should be included in the same commit whenever practical.

---

# Compliance

Work should not be considered complete until all affected documentation has been reviewed and updated.

Documentation quality is part of the project's overall quality standards.

---

End of Documentation Policy.