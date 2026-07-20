# Project Structure Guidelines

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document defines the structural principles that should guide the organization of the AI Studio codebase.

A consistent project structure improves maintainability, discoverability, and long-term scalability.

---

# Core Principles

The repository should remain:

- Modular
- Predictable
- Easy to navigate
- Easy to extend
- Easy to test

---

# Separation of Responsibilities

Each directory should have a single, well-defined purpose.

Examples include:

- Application code
- Templates
- Static assets
- Configuration
- Documentation
- Tests
- Runtime workspace

Responsibilities should not overlap.

---

# Module Organization

Modules should:

- Have a single responsibility.
- Minimize dependencies.
- Expose clear interfaces.
- Avoid circular imports.

Large modules should be split into smaller components when appropriate.

---

# Service Layer

Business logic belongs in service modules.

Services should:

- Be reusable.
- Be independent of presentation logic.
- Avoid direct user interface responsibilities.

---

# Route Layer

Routes should:

- Validate requests.
- Delegate business logic to services.
- Return responses.

Routes should remain lightweight.

---

# Templates

Templates should:

- Focus on presentation.
- Avoid embedding business logic.
- Reuse common layouts where practical.

---

# Static Assets

Static resources should be organized by type.

Typical categories include:

- CSS
- JavaScript
- Images
- Icons

Assets should use descriptive names.

---

# Tests

Test organization should mirror the application structure whenever practical.

Each major module should have corresponding tests.

---

# Documentation

Documentation belongs under:

```text
docs/
```

Historical documentation belongs under:

```text
docs/old/
```

Milestone documentation belongs under:

```text
docs/milestones/
```

---

# Runtime Data

Generated application data belongs in the workspace directory.

Runtime data should never be mixed with source code.

---

# Future Growth

When introducing new components:

- Reuse existing directories whenever possible.
- Create new top-level directories only when justified.
- Update repository documentation if the structure changes.

---

# Review Checklist

Before introducing structural changes, verify:

- Responsibilities remain clear.
- Existing architecture is preserved.
- Documentation is updated.
- Tests continue to pass.

---

End of Project Structure Guidelines.