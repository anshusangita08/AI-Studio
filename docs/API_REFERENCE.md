# API Reference

Version: 1.0

Status: Living Documentation

---

# Purpose

This document provides a high-level reference for the HTTP API exposed by AI Studio.

It serves as a developer reference for routes, request flow, and endpoint responsibilities.

Detailed implementation remains within the source code.

---

# API Design Principles

The API should be:

- REST-oriented where practical
- Predictable
- Consistent
- Easy to extend
- Easy to test

---

# Request Flow

```text
Browser
    │
    ▼
FastAPI Route
    │
    ▼
Service Layer
    │
    ▼
Filesystem
    │
    ▼
Response
```

---

# Route Responsibilities

Routes should:

- Receive HTTP requests
- Validate request data
- Call the appropriate service
- Return HTML or JSON responses
- Avoid implementing business logic

---

# Response Types

The application may return:

- HTML
- JSON
- Redirect responses
- Error responses

The response format depends on the requesting component.

---

# HTTP Methods

## GET

Used for:

- Displaying pages
- Loading data
- Reading resources

GET requests should not modify application state.

---

## POST

Used for:

- Creating resources
- Updating resources
- Executing actions

---

## PUT

Reserved for complete resource replacement where appropriate.

---

## DELETE

Used for resource deletion.

Deletion should be validated before execution.

---

# Endpoint Categories

## Project Management

Typical operations include:

- List projects
- Create project
- Rename project
- Delete project
- Open project

---

## Story Planning

Typical operations include:

- Load story
- Save story
- Expand story
- Generate story
- Generate scenes

---

## Scene Management

Typical operations include:

- List scenes
- Save scenes
- Update scenes
- Delete scenes

---

## Asset Management

Future functionality may include:

- Images
- Audio
- Video
- Generated assets

---

## Settings

Configuration-related endpoints may include:

- Application settings
- AI configuration
- Workspace configuration

---

# Validation

Routes should validate:

- Required fields
- Invalid values
- File paths
- Request format

Invalid requests should return meaningful error responses.

---

# Error Responses

Error responses should:

- Explain the problem
- Avoid exposing implementation details
- Support troubleshooting

---

# Authentication

Current versions operate as a local application.

Authentication requirements may change in future versions if remote access is introduced.

---

# API Evolution

When introducing new endpoints:

- Preserve consistency.
- Reuse existing services.
- Follow naming conventions.
- Update this document if endpoint categories change significantly.

---

End of API Reference.