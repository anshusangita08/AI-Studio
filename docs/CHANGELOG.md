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

## Milestone 011 – Export Implementation

### Added

- Export route exposing `/export/<slug>` endpoint.
- Export Project UI button on Project Details page.
- ZIP archive generation with timestamped filename.
- `manifest.json` generation inside the export package.
- Exclusion of `cache/`, `temp/`, and `exports/` directories from the archive.

### Changed

- ProjectService now orchestrates exports via ExportService.

### Testing

- Added export tests covering ZIP creation, manifest content, and exclusion rules.
- Full test suite passing (44/44).

---

## Milestone 012 – Rendering / Video Assembly

### Added

- RenderService implementation for rendering projects.
- POST /projects/{slug}/render exposing rendering functionality.
- Render Project action added to the project details page UI.
- `render/render.json` created with status and timestamp upon rendering.

### Changed

- ProjectService integrated with RenderService for orchestration.

### Testing

- Added tests verifying render JSON creation and endpoint behavior.
- Full test suite passing (43/43).

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
