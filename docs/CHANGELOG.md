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

## Milestone 013 – UI Polish and Design System Refinement

### Added

- Reusable design system utilities for layout, spacing, typography, and forms.
- Consistent editor layouts for Story, Expanded Story, and Scenes.
- Improved accessibility with semantic headings and associated form labels.
- Responsive layout refinements across project and Story Planner pages.

### Changed

- Refined global styling in `theme.css` and project-specific styling in `project.css`.
- Updated templates to consistently use the project's design system and utility classes.
- Improved Project Index, Project Details, and Story Planner layouts for visual consistency.
- Standardized editor spacing, typography, and action layouts.

### Testing

- Full UI regression testing completed.
- Full automated test suite passing (44/44).

---
## Milestone 014 – Asset Workspace Foundation

### Added

- Automatic creation of project asset directories:
  - assets/images
  - assets/audio
  - assets/video
- Render metadata now includes placeholder collections for image, audio, and video assets.

### Changed

- Project creation now initializes the asset workspace.
- Render metadata prepared for future asset generation workflows.

### Testing

- Added automated tests for asset workspace creation.
- Added automated tests for render metadata placeholders.
- Full automated test suite passing (46/46).

---
## Milestone 015.1 – Prompt Template Engine

### Added

- Introduced a standalone `PromptTemplateEngine` for lightweight placeholder rendering.
- Added support for placeholder replacement using plain Python.
- Unknown placeholders are preserved to support future template expansion.

### Changed

- None

### Testing

- Added automated unit tests covering placeholder rendering behavior.
- Full automated test suite passing (54/54).

---

## Milestone 015.2 – PromptService Integration

### Added

- Integrated PromptTemplateEngine into PromptService.

### Changed

- Prompt generation now delegates placeholder rendering to PromptTemplateEngine while preserving existing behavior.

### Testing

- Full automated test suite passing (54/54).
---

## Milestone 015.3 – Prompt Context Builder

### Added

- Structured prompt context generation for template rendering.

### Changed

- PromptService now builds and supplies structured context to PromptTemplateEngine.

### Testing

- Added unit tests for context construction and template integration.
- Full automated test suite passing (57/57).
---

## Milestone 015.4 – Prompt Template Expansion

### Changed

- Replaced hard-coded prompt construction with a reusable prompt template.
- Prompt templates are rendered through PromptTemplateEngine.
- Existing prompt output preserved.

### Testing

- Updated PromptService tests.
- Full test suite passing (57/57).
---

## Milestone 015.5 – Prompt Template Library

### Added

- Introduced a shared prompt template library.

### Changed

- PromptService now imports reusable prompt templates from a dedicated module.

### Testing

- Full automated test suite passing (57/57).
---

## Milestone 015.6 – Prompt Template Variants

### Added

- Added reusable image and narration prompt template definitions.

### Changed

- Expanded the shared prompt template library for future prompt types.

### Testing

- Full automated test suite passing (57/57).
---

## Milestone 015.7 – Typed Prompt Generation

### Added

- Added generate_image_prompt().
- Added generate_narration_prompt().

### Changed

- Centralized prompt rendering through a shared private helper.

### Testing

- Full automated suite passing (59/59).
---

## Milestone 015.8 – Structured Image Prompt Generation

### Added

- Added structured image prompt generation with default visual metadata.

### Changed

- IMAGE_PROMPT_TEMPLATE now renders style, composition, camera, lighting, quality, and negative prompt fields.

### Testing

- Full automated suite passing (59/59).
---

## Milestone 015.9 – Structured Narration Prompt Generation

### Added

- Structured narration prompt generation with narration-specific defaults.

### Changed

- NARRATION_PROMPT_TEMPLATE now renders narration style, tone, pacing, voice style, target duration, and delivery notes.

### Testing

- Full test suite passing (59/59).
---

## Milestone 016.0 – LM Studio Prompt Integration Foundation

### Added

- Integrated PromptService with the existing LMStudioClient.
- Added a reusable internal prompt execution helper for future AI-powered workflows.

### Changed

- PromptService now owns LM Studio prompt execution while preserving the existing prompt rendering pipeline.

### Testing

- Full automated test suite passing (59/59).

---

## Milestone 016.1 – AI Story Generation

### Added

- PromptService now supports AI-powered story generation through LM Studio.

### Changed

- Story generation now executes through the PromptService AI pipeline.

### Testing

- Updated PromptService tests.
- Full automated test suite passing (61/61).
---

## Milestone 017 – StoryService Integration

### Changed

- StoryService now delegates story generation to PromptService while preserving the existing public interface.

### Testing

- Updated StoryService tests.
- Full automated test suite passing (61/61).
---

## Milestone 018 – Route Integration Verification

### Verified

- Confirmed the existing Story Planner route already delegates to StoryService.
- No implementation changes were required.

### Testing

- Architecture verified.
- No production code changes.
---

## Milestone 019 – End-to-End Story Generation Verification

### Added

- AI-powered scene generation using LM Studio.
- End-to-end Story → Expanded Story → Scenes workflow.
- Automatic persistence of generated scenes to `scenes.md`.

### Changed

- PromptService now supports AI-powered scene generation.
- Story Planner now supports the complete AI-assisted story planning workflow from story generation through scene generation.
- Improved LM Studio request logging and diagnostics for troubleshooting.

### Fixed

- Replaced the previous mock scene generation workflow with the production AI generation pipeline.
- Resolved coroutine-related issues by using the synchronous LM Studio client implementation.

### Testing

- Full automated test suite passing (61/61).
- End-to-end Story → Expanded Story → Scenes workflow manually verified.
- Verified generation and persistence of `story.md`, `expanded_story.md`, and `scenes.md`.
---


## Unreleased

### Added

- End-to-end LM Studio integration for AI story generation.
- Story expansion now executes against the configured local language model.
- Additional debug logging for LM Studio request and response troubleshooting.

### Changed

- Replaced the asynchronous LM Studio client with a synchronous requests-based implementation.
- PromptService now executes rendered prompts directly through LM Studio.
- StoryService now performs real AI story generation instead of mock generation.

### Fixed

- Resolved coroutine execution issues during story generation.
- Improved LM Studio error reporting for invalid requests and configuration problems.
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
