# AI Studio Standard Workflow

## Phase 1 — Planning

Goal:
Understand the requested milestone without modifying code.

Tasks:

- Read CLINE.md
- Read .clinerules
- Read PROMPTS.md
- Analyze the repository
- Identify affected files
- Produce:
  - Architecture summary
  - Implementation plan
  - Risks
  - Test strategy

Do not modify files.

Wait for approval.

---

## Phase 2 — Implementation

After approval:

- Modify only approved files.
- Keep architecture unchanged.
- Keep code modular.
- Explain important design decisions.

---

## Phase 3 — Validation

Run:

python -m pytest

If tests fail:

- Fix failures.
- Run pytest again.
- Repeat until successful or blocked.

---

## Phase 4 — Completion

Return:

- Files changed
- Tests executed
- Test results
- Remaining TODOs

Never commit unless explicitly instructed.