# AI Development Workflow

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document defines how AI assistants are used during development.

It establishes responsibilities, expectations, and rules for AI-assisted development while preserving a consistent architecture and coding style.

---

# Primary Development Environment

## IDE

- Visual Studio Code

## Local AI Runtime

- LM Studio

## API

- OpenAI Compatible API

---

# AI Assistants

## ChatGPT

Primary responsibilities:

- Architecture
- Planning
- Documentation
- Design reviews
- Debugging
- Technical decisions
- Code reviews
- Milestone planning

---

## Aider

Primary responsibilities:

- Multi-file implementation
- Repository-wide changes
- Refactoring
- Feature implementation

---

## Continue

Primary responsibilities:

- Small scoped implementation
- Local code completion
- File editing
- Quick fixes

---

## Cline

Primary responsibilities:

- Repository exploration
- Context-aware assistance
- Small implementation tasks

---

# Local Models

Models may change over time.

Current reference models include:

- GPT-OSS
- Qwen

---

# Development Process

Every implementation should follow this workflow.

1. Understand the requirement.
2. Review existing implementation.
3. Review architecture.
4. Create an implementation plan.
5. Modify the minimum required files.
6. Test the implementation.
7. Perform manual verification.
8. Update documentation.
9. Commit changes.

---

# Implementation Rules

Always:

- Read existing code first.
- Preserve architecture.
- Reuse existing services.
- Keep changes small.
- Maintain readability.
- Test before completion.

Never:

- Rewrite working code unnecessarily.
- Introduce unrelated changes.
- Change architecture without approval.
- Add unnecessary dependencies.
- Refactor unrelated modules.

---

# Documentation Updates

When work is completed:

- Update PROGRESS.md
- Update the current milestone document
- Update CHANGELOG.md when appropriate

---

# AI Output Expectations

AI-generated code should:

- Match project conventions.
- Be production quality.
- Be readable.
- Include appropriate error handling.
- Avoid unnecessary complexity.

---

# Review Checklist

Before accepting AI-generated changes:

- Architecture preserved
- Existing functionality unaffected
- Tests completed
- Manual verification completed
- Documentation updated

---

End of AI Development Workflow.