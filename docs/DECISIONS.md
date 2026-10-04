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
| ADR-002 | 2026-10-04 | Enforce step-by-step, understanding-first teaching with concrete relevant examples and no unexplained jumps | Accepted |

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


## ADR-002 — Non-Negotiable Understanding-First Teaching Contract

- **Date:** 2026-10-04
- **Status:** Accepted
- **Applies to:** Both

### Context
The learner's goal is deep ML/DL engineering competence rather than fast topic completion. Explanations that stay at a vague or top-level survey level, jump over intermediate reasoning, or use examples that do not materially help understanding create false familiarity instead of durable understanding.

### Decision
All instructional work in this program must follow an understanding-first, step-by-step teaching contract. This is **non-negotiable** and applies across topics, stages, sessions, and future chats that resume from this repository.

For every new or weak concept:
1. Start from the concrete problem or question the concept solves.
2. Explain why the problem matters and what a naive or simpler approach would do.
3. Show what limitation, failure, inefficiency, or ambiguity motivates the new concept.
4. Derive the core idea in simple language without skipping intermediate reasoning.
5. Use a small, concrete example whose data and behavior directly illuminate the concept; do not use vague analogies or examples unrelated to the actual mechanism.
6. Only then introduce syntax, APIs, formulas, or implementation details.
7. Inspect or predict outputs and connect them back to the concept.
8. Explicitly cover common confusions/failure modes.
9. Require the learner to explain or apply the concept before marking it understood.
10. Connect the concept to its real ML/data/engineering use when relevant.

Do not optimize for finishing the curriculum quickly. Do not jump ahead because a topic appears familiar. Do not compress a concept until understanding has been demonstrated. When the learner starts with zero knowledge, teach from first principles rather than using a diagnostic-only survey.

### Rationale
This program targets high-end ML/DL engineering capability. Durable mental models, transfer to unfamiliar problems, debugging ability, and correct reasoning are more important than covering a larger number of APIs or topics superficially.

### Alternatives Considered
- High-level API survey followed by later practice — rejected because it creates shallow familiarity and leaves the learner unable to derive or debug behavior.
- Fast examples without mechanism-level explanation — rejected because examples are only useful when they clarify why the concept works.
- Compressing based on prior exposure alone — rejected; compression is allowed only after demonstrated competence.

### Consequences
Lessons may take longer and use more intermediate checks. Topic completion dates are secondary to demonstrated understanding. Teaching state should record real gaps rather than silently progressing past them.

### Revisit Trigger
Revisit only if the learner explicitly changes the learning objective or requests a different teaching contract.
