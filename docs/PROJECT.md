# AI Studio

Version: 1.0  
Status: Project Definition

---

# Vision

AI Studio is a production-quality, local-first AI Video Creation application.

The objective is to provide an end-to-end workflow for generating AI videos entirely on local hardware without requiring cloud services.

The project is designed for long-term maintainability, modularity, and incremental development.

---

# Project Goals

- Run completely offline
- Use local AI models
- Preserve user privacy
- Modular architecture
- Production-quality implementation
- Simple and maintainable codebase
- Desktop-first workflow
- No unnecessary complexity

---

# Core Features

Current and planned capabilities include:

- Project Management
- Story Planning
- Story Generation
- Expanded Story Generation
- Scene Planning
- Prompt Generation
- Image Generation
- Speech Generation
- Video Compilation

Features are implemented incrementally through project milestones.

---

# Technology Stack

## Backend

- Python
- FastAPI

## Frontend

- HTML
- HTMX
- Jinja2
- Minimal JavaScript

## AI

- LM Studio
- OpenAI Compatible API

## Primary Development Models

- GPT-OSS
- Qwen

## Image

- Pillow
- Fooocus (planned)

## Speech

- Edge TTS

## Video

- FFmpeg

## Storage

- Local filesystem only
- No database

## Platform

- Windows

---

# Repository Structure

```text
app/            Application source code
config/         Configuration files
docs/           Project documentation
tests/          Automated tests
workspace/      Runtime project workspace
```

---

# Development Workflow

Development follows an incremental milestone-based process.

Each feature is implemented using the following workflow:

1. Review the current implementation.
2. Review the architecture.
3. Review the milestone requirements.
4. Identify the smallest logical implementation step.
5. Implement only that step.
6. Test the implementation.
7. Perform manual verification where appropriate.
8. Update documentation.

Large changes should be divided into multiple smaller implementation steps.

---

# AI Development Workflow

AI assistance is a core part of this project's development process.

Current development environment:

## IDE

- Visual Studio Code

## AI Assistants

### ChatGPT

Primary responsibilities:

- Architecture
- Planning
- Design reviews
- Code reviews
- Debugging
- Documentation
- Milestone planning

### Aider

Primary responsibilities:

- Large multi-file implementations
- Repository-wide edits
- Refactoring within existing architecture

### Continue

Primary responsibilities:

- Small scoped edits
- Local code completion
- Minor implementation tasks

### Cline

Primary responsibilities:

- Repository exploration
- Context-aware assistance
- Small implementation tasks

### LM Studio

Provides local AI inference using the OpenAI-compatible API.

Current reference models:

- GPT-OSS
- Qwen

Models may change over time without affecting the project architecture.

---

# Development Principles

The following principles guide all implementation work.

- Preserve the existing architecture.
- Keep modules small and focused.
- Keep functions simple.
- Reuse existing services whenever practical.
- Prefer extending existing functionality over rewriting it.
- Avoid unnecessary abstractions.
- Avoid unnecessary refactoring.
- Maintain backward compatibility whenever practical.
- Never redesign the application without explicit approval.

---

# Coding Standards

- Read existing code before modifying it.
- Follow the existing coding style.
- Modify the minimum number of files necessary.
- Never perform cosmetic changes unrelated to the task.
- Never rewrite working code without a valid reason.
- Keep implementation readable and maintainable.

---

# Testing Standards

Every implementation should be verified before completion.

Testing may include:

- Unit tests
- Integration tests
- Manual verification

Implementation is not considered complete until testing has been performed.

---

# Documentation Standards

Documentation follows the rules defined in `REPOSITORY_RULES.md`.

In summary:

- Every topic has one authoritative document.
- Documentation reflects the implementation.
- Project status is maintained only in `PROGRESS.md`.
- Architecture is maintained only in `ARCHITECTURE.md`.

---

# Git Workflow

Development is performed on feature or development branches.

General principles:

- Keep the main branch stable.
- Keep commits focused.
- Test before committing.
- Avoid unrelated changes within the same commit.

---

End of Project Definition.