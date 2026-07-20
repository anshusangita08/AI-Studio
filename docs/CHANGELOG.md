# Changelog

Version: 1.0

---

# Purpose

This document records released milestones and significant project changes.

It is intended to provide a chronological history of the project without describing implementation details.

Implementation details belong in milestone documents.

---

# Entry Format

Each release should contain:

- Version or milestone
- Release date
- Summary
- Major additions
- Breaking changes (if any)

---

# Releases

## Milestone 009 – Prompt Engine Implementation

### Added

- Prompt Service module for dynamic prompt generation.
- Integration points with existing services.

### Changed

- Updated project structure to include `app/services/prompt_service.py`.
- Minor refactoring of service registry to accommodate new engine.

### Fixed

- None

---

## Milestone 010 – Project Pipeline Completion

### Added

- Backend pipeline status orchestration across StoryService, PromptService and ProjectService.
- UI integration: Project Pipeline card with overall status and progress indicator.
- Progress calculation moved from template to route logic.
- Updated project details page to display pipeline status.

### Changed

- None

### Fixed

- None

---

## Unreleased

### Added

- None

### Changed

- None

### Fixed

- None

---

## Template

### Version

vX.Y.Z or Milestone XXX

### Date

YYYY-MM-DD

### Added

-

### Changed

-

### Fixed

-

### Removed

-

### Notes

Optional

---

# Guidelines

- Record only completed work.
- Keep entries concise.
- Do not include implementation details.
- Reference milestone documents for technical information.

---

End of Changelog.
