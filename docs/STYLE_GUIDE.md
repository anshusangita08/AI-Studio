# Documentation Style Guide

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document defines the writing standards for all documentation in AI Studio.

The goal is to keep documentation consistent, readable, and easy to maintain.

---

# General Principles

Documentation should be:

- Clear
- Concise
- Accurate
- Consistent
- Easy to update

Avoid unnecessary detail where another document already serves as the source of truth.

---

# Writing Style

Use:

- Short sentences.
- Simple language.
- Active voice.
- Consistent terminology.
- Present tense where appropriate.

Avoid:

- Ambiguous wording.
- Personal opinions.
- Marketing language.
- Unverified assumptions.

---

# Headings

Use a logical heading hierarchy.

Example:

```text
# Title

## Section

### Subsection
```

Do not skip heading levels.

---

# Lists

Use bullet lists for unordered information.

Example:

- Item one
- Item two
- Item three

Use numbered lists only when sequence matters.

---

# Code Blocks

Specify the language whenever possible.

Example:

```python
print("Hello World")
```

Use plain text blocks for directory structures and generic examples.

---

# File Paths

Always format repository paths using inline code.

Example:

`docs/README.md`

---

# Commands

Command-line examples should use fenced code blocks.

Example:

```bash
python launcher.py
```

---

# Tables

Use tables only when they improve readability.

Avoid tables for simple lists.

---

# Cross References

Reference documents by their repository path.

Example:

- `docs/ARCHITECTURE.md`
- `docs/PROJECT.md`

Avoid duplicating information that already exists elsewhere.

---

# Version Information

Permanent documents should include:

- Version
- Status

near the top of the document.

---

# Status Values

Recommended status values:

- Permanent Documentation
- Living Documentation
- Historical Documentation
- Template

---

# Maintenance

When updating documentation:

- Keep formatting consistent.
- Remove obsolete information.
- Update related documents if necessary.
- Preserve the single source of truth.

---

# Review Checklist

Before committing documentation:

- Grammar checked
- Spelling checked
- Formatting consistent
- Headings correct
- Links valid
- No duplicate information
- Examples verified

---

End of Documentation Style Guide.