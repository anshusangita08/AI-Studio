# Architecture Decision Log

Version: 1.1

Status: Permanent Documentation

---

# Purpose

This document records significant architectural and long-term technical decisions made throughout the lifetime of AI Studio.

It explains **why** a decision was made rather than **how** it was implemented.

Implementation details, code changes, and feature progress belong in milestone documents and the project changelog.

---

# Scope

This document records decisions that have long-term impact on the project, including:

- Architecture
- Technology selection
- Development workflow
- Project organization
- Long-term engineering standards
- Major design changes

Routine feature development should **not** be recorded here.

---

# Decision Lifecycle

Each Architecture Decision Record (ADR) should have one of the following statuses:

- Proposed
- Accepted
- Superseded
- Deprecated

Historical decisions should never be deleted.

If a decision changes:

1. Leave the original ADR unchanged.
2. Mark its status as **Superseded**.
3. Create a new ADR describing the replacement.

This preserves the engineering history of the project.

---

# Decision Index

| ADR | Title | Status |
|------|-------|--------|
| ADR-0001 | Local-First Architecture | Accepted |
| ADR-0002 | Filesystem Storage | Accepted |
| ADR-0003 | Incremental Milestone Development | Accepted |

---

# ADR Template

## ADR-XXXX

### Date

YYYY-MM-DD

### Title

Short descriptive title.

### Status

Proposed / Accepted / Superseded / Deprecated

### Context

Describe the problem, requirement, or situation that led to the decision.

### Decision

Describe the chosen solution.

### Consequences

Describe the long-term effects of the decision, including advantages, trade-offs, and limitations.

---

# Architecture Decision Records

---

## ADR-0001

### Date

YYYY-MM-DD

### Title

Local-First Architecture

### Status

Accepted

### Context

The project required complete offline capability while preserving user privacy and minimizing external dependencies.

### Decision

Adopt a local-first architecture using locally hosted AI models and filesystem-based project storage.

### Consequences

- No cloud dependency
- User data remains on the local machine
- Offline operation is fully supported
- Higher local hardware requirements
- AI performance depends on available hardware

---

## ADR-0002

### Date

YYYY-MM-DD

### Title

Filesystem Storage

### Status

Accepted

### Context

The application required a simple, portable, and maintainable persistence mechanism without introducing unnecessary infrastructure.

### Decision

Store project data using the local filesystem instead of a relational or NoSQL database.

### Consequences

- Simplified deployment
- Easy backup and restore
- Human-readable project files
- Minimal maintenance overhead
- Limited support for concurrent multi-user editing

---

## ADR-0003

### Date

YYYY-MM-DD

### Title

Incremental Milestone Development

### Status

Accepted

### Context

The project is developed iteratively with AI assistance and requires frequent verification of completed functionality.

### Decision

Adopt milestone-based development where each milestone delivers a complete, testable feature before progressing to the next.

### Consequences

- Smaller implementation scope
- Easier code reviews
- Better regression testing
- Improved documentation quality
- Clear project history

---

# Future ADR Candidates

The following are examples of decisions that may eventually become ADRs if adopted:

- FastAPI as the backend framework
- HTMX for progressive enhancement
- Jinja2 server-side rendering
- OpenAI-compatible inference interface
- LM Studio as the default local inference engine
- Plugin architecture
- Asset pipeline redesign
- Export framework
- Workflow engine
- Multi-user collaboration support

---

# Guidelines

- Record only long-term engineering decisions.
- One ADR should describe one decision.
- Keep each ADR concise and focused.
- Never modify historical decisions except to update their status.
- Add new ADRs rather than rewriting old ones.
- Reference related ADRs where appropriate.
- Use sequential numbering.

---

# Related Documents

- ARCHITECTURE.md
- ARCHITECTURE_PRINCIPLES.md
- PROJECT_PHILOSOPHY.md
- CHANGELOG.md
- ROADMAP.md

---

End of Architecture Decision Log.