# DECISIONS — Shared Program ADR Log

This is the single shared append-only decision log for both ML and DL tracks.

Use it for durable choices that should survive across sessions, such as:

- primary cloud provider;
- orchestration platform;
- experiment tracker/model registry;
- data/versioning strategy;
- deployment/runtime choices;
- important project architecture decisions;
- pace/scope changes that affect the program;
- replacing one previously accepted tool/approach with another.

Do **not** duplicate curriculum rules here. Curriculum requirements remain in their curriculum files.

## Rules

1. Append new decisions; do not rewrite history.
2. Every decision has a stable ADR number.
3. If replaced, mark the old decision `Superseded by ADR-XXX` and add a new ADR.
4. Record rationale and meaningful alternatives, not only the selected tool.
5. Do not create a decision just because a tool was mentioned in a lesson.

---

## Decision Index

| ADR | Date | Decision | Status |
|---|---|---|---|
| — | — | No durable implementation/tooling decision recorded yet | — |

---

## ADR Template

```markdown
## ADR-XXX — <Short Decision Title>

- **Date:** YYYY-MM-DD
- **Status:** Proposed | Accepted | Superseded by ADR-YYY
- **Applies to:** ML | DL | Both

### Context
What durable problem or constraint requires a decision?

### Decision
What was selected?

### Rationale
Why is this the best current choice?

### Alternatives Considered
- Alternative A — reason not selected
- Alternative B — reason not selected

### Consequences
What becomes easier/harder? What migration/cost/maintenance implications exist?

### Revisit Trigger
What evidence or future condition should cause this decision to be reconsidered?
```