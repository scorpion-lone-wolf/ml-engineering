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
| ADR-001 | 2026-09-16 | Use Conda for local Python environment/interpreter management; teach pip fundamentals and introduce uv after packaging basics | Accepted |

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

## ADR-001 — Local Python Environment and Dependency Tooling

- **Date:** 2026-09-16
- **Status:** Accepted
- **Applies to:** ML (and reusable for DL unless later superseded)

### Context
The learner's machine uses Anaconda/Conda as the available Python distribution rather than a separately installed system Python. Stage 0 needs a workflow that is practical locally while still teaching industry-standard Python packaging concepts.

### Decision
Use **Conda** to create and activate isolated local project environments/interpreters (for example, a project-local path environment such as `.venv`). Teach **pip semantics and commands** because pip literacy is broadly transferable and required to understand Python packaging behavior. Use `pyproject.toml` for modern project metadata/direct dependency declaration. Introduce **uv** after the pip/`pyproject.toml` fundamentals are understood, primarily for modern dependency resolution/locking/install workflows where it improves reproducibility and speed. Do not treat uv as a replacement for understanding pip or Python packaging concepts.

### Rationale
- Conda matches the learner's installed Python distribution and already works correctly on the machine.
- pip remains foundational ecosystem knowledge even when another installer/resolver is used.
- `pyproject.toml` is the modern standardized project configuration/dependency declaration location.
- uv is increasingly useful for fast installs and lock/reproducibility workflows, but introducing it after the fundamentals avoids hiding the mechanics being learned.

### Alternatives Considered
- System Python + `venv` only — unnecessary because the learner does not maintain a separate system Python installation.
- Conda-only dependency management for every package — workable, but would underexpose standard PyPI/pip packaging workflows used widely in ML/software projects.
- uv-only from the first lesson — modern and fast, but would hide some foundational environment/package-management concepts the learner should first understand.

### Consequences
Local exercises may use Conda commands for environment creation/activation rather than `python -m venv`. Curriculum explanations should distinguish the environment manager from the dependency declaration/lock mechanism. Exact lockfile workflow is taught in Stage 0 dependency-management lessons and may be refined without changing the environment-manager choice.

### Revisit Trigger
Revisit if Conda materially complicates CI/CD, Docker, deployment, GPU/CUDA package resolution, or a later project benefits from standardizing on a different environment workflow.
