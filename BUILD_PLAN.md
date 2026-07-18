# AI Studio - Master Build Plan

Version: 1.0
Status: Living Document

---

# Project Vision

AI Studio is a production-quality Local AI Video Factory.

Everything runs locally.

No cloud AI.

Modular architecture.

Professional quality.

Simple UI.

Built for long-term maintainability.

---

# Architecture Summary

Backend
- Python 3.12+
- FastAPI

Frontend
- HTMX
- Jinja2
- HTML/CSS

AI
- LM Studio (OpenAI compatible API)

Image
- Pillow
- Fooocus (future)

Speech
- Edge TTS

Video
- FFmpeg

---

# Coding Standards

Never redesign architecture unless explicitly instructed.

Modify the minimum number of files.

Reuse existing services.

Never invent APIs.

Inspect implementations before coding.

Keep functions small.

Keep modules independent.

Prefer extending existing services.

Never rewrite working code.

Never break previous milestones.

---

# Milestone Index

- [Milestone 001–006](docs/milestones/001-006-foundation.md) - Foundation
- [Milestone 007](docs/milestones/007-project-manager.md) - Project Manager
- [Milestone 008.1](docs/milestones/008.1-story-editor.md) - Story Editor
- [Maintenance](docs/milestones/maintenance.md) - Maintenance
- [Milestone 008.2](docs/milestones/008.2-story-generation-mock.md) - Story Generation (Mock)
- [Milestone 008.3](docs/milestones/008.3-lm-studio-integration.md) - LM Studio Integration
- [Milestone 009](docs/milestones/009-story-templates.md) - Story Templates
- [Milestone 010](docs/milestones/010-character-manager.md) - Character Manager
- [Milestone 011](docs/milestones/011-scene-planner.md) - Scene Planner
- [Milestone 012](docs/milestones/012-prompt-generator.md) - Prompt Generator
- [Milestone 013](docs/milestones/013-image-engine.md) - Image Engine
- [Milestone 014](docs/milestones/014-speech-engine.md) - Speech Engine
- [Milestone 015](docs/milestones/015-story-compiler.md) - Story Compiler
- [Milestone 008.5](docs/milestones/008.5-project-manager.md) - Project Manager (CRUD)

---

# Current Milestone

Milestone 008.5
---

# Links to milestone documents

All milestone documentation is now in the docs/milestones directory.