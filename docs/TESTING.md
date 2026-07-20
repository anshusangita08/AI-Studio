# Testing Guide

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document defines the testing standards followed throughout AI Studio development.

---

# Objectives

Testing ensures that:

- Features behave as expected.
- Existing functionality is not broken.
- Project stability is maintained.
- Changes are verified before merging.

---

# Testing Types

## Unit Testing

Tests individual functions and services.

Focus areas include:

- Business logic
- Validation
- Utilities
- File operations

---

## Integration Testing

Tests interactions between components.

Examples include:

- Route → Service
- Service → Filesystem
- End-to-end feature workflow

---

## Manual Testing

Manual verification is required for user-facing functionality.

Typical areas include:

- User interface
- HTMX interactions
- Project workflows
- Story workflow
- Scene workflow
- AI integration

---

# Test Principles

- Test every new feature.
- Test bug fixes.
- Test edge cases where practical.
- Keep tests independent.
- Keep tests repeatable.
- Prefer automated tests whenever possible.

---

# Test Organization

```text
tests/
├── unit/
├── integration/
└── fixtures/
```

Adjust the structure as the project evolves.

---

# Test Data

- Use isolated test data.
- Avoid modifying production workspace data.
- Clean up temporary files after tests complete.

---

# Regression Testing

Before completing any milestone, verify:

- Existing tests pass.
- Core workflows continue to function.
- Previously fixed bugs have not returned.

---

# Manual Verification Checklist

Typical verification includes:

- Application starts successfully.
- Routes load correctly.
- Forms submit successfully.
- Data persists correctly.
- Files are created correctly.
- Existing functionality remains operational.

---

# Completion Criteria

A task is considered complete only after:

- Required implementation is finished.
- Testing is completed.
- Manual verification is completed where applicable.
- Documentation is updated.

---

End of Testing Guide.