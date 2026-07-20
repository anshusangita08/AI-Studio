# Frequently Asked Questions

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document answers common questions about AI Studio, its architecture, and its development workflow.

---

# General

## What is AI Studio?

AI Studio is a local-first AI video creation application designed to run entirely on local hardware.

---

## Does AI Studio require internet access?

No.

The application is designed to function locally using locally hosted AI models.

Internet access may be required only for downloading models, dependencies, or software updates.

---

## Why is there no database?

The project uses filesystem-based persistence.

This simplifies deployment, backups, portability, and maintenance.

---

## Why use LM Studio?

LM Studio provides a local OpenAI-compatible API that allows different language models to be used without changing the application architecture.

---

## Can AI models be changed?

Yes.

The application is designed to support different local models through the same OpenAI-compatible interface.

---

# Development

## Where should I start reading?

Read the documentation in this order:

1. PROJECT.md
2. ARCHITECTURE.md
3. CODING_STANDARDS.md
4. TESTING.md
5. PROGRESS.md

---

## Where is the current project status?

Only in:

`docs/PROGRESS.md`

---

## Where are architectural decisions documented?

`docs/DECISIONS.md`

---

## Where are completed milestones documented?

`docs/milestones/`

---

## Where are old documents stored?

`docs/old/`

---

# Documentation

## Which document is updated most often?

`PROGRESS.md`

---

## Which documents rarely change?

- README.md
- PROJECT.md
- ARCHITECTURE.md
- CODING_STANDARDS.md
- TESTING.md
- AI_WORKFLOW.md
- CONTRIBUTING.md
- DEPENDENCIES.md
- DECISIONS.md
- FAQ.md

---

## Should documentation be duplicated?

No.

Each topic should have exactly one authoritative document.

---

# Source of Truth

If documentation and implementation differ, the implementation is considered authoritative until the documentation is updated.

---

End of Frequently Asked Questions.