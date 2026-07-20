# Dependencies

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document defines the dependency policy for AI Studio.

It explains which dependencies are used, why they are used, and the rules for introducing new dependencies.

---

# Principles

Dependencies should be:

- Necessary
- Stable
- Well maintained
- Actively supported
- Compatible with the project architecture

Prefer the Python Standard Library whenever practical.

---

# Backend

| Dependency | Purpose |
|------------|---------|
| Python | Programming language |
| FastAPI | Web framework |
| Uvicorn | ASGI server |
| Jinja2 | Server-side templates |
| HTMX | Dynamic user interface |

---

# AI

| Dependency | Purpose |
|------------|---------|
| LM Studio | Local AI runtime |
| OpenAI Compatible API | Model communication |

---

# Media

| Dependency | Purpose |
|------------|---------|
| Pillow | Image processing |
| FFmpeg | Video processing |
| Edge TTS | Speech generation |

---

# Testing

| Dependency | Purpose |
|------------|---------|
| pytest | Automated testing |

---

# Dependency Rules

Before adding a dependency:

- Verify that existing libraries cannot solve the problem.
- Prefer lightweight solutions.
- Avoid duplicate functionality.
- Consider long-term maintenance.
- Verify license compatibility.

---

# Updating Dependencies

When updating:

- Review release notes.
- Verify compatibility.
- Run automated tests.
- Perform manual verification.
- Update documentation if required.

---

# Removing Dependencies

A dependency should be removed when:

- It is no longer used.
- It is no longer maintained.
- It creates unnecessary complexity.
- A better supported alternative exists.

---

# Version Management

- Prefer stable releases.
- Avoid unnecessary upgrades.
- Upgrade deliberately.
- Test after every upgrade.

---

End of Dependencies.