# ML LEARNING STATE — Demonstrated Understanding

> Track 1 learner-understanding source of truth. Update the current snapshot as learning progresses; preserve checkpoint/history sections.

## Current Snapshot

- **Track:** Track 1 — Classical ML + Production ML/MLOps
- **State:** LEARNING
- **Current stage:** Stage 0 — Environment and Engineering Setup
- **Current topic:** Python package/import structure, then configuration/environment variables
- **Last mastered topic:** Stage 0 environment isolation, dependency declaration, direct/transitive dependencies, locking, and exact environment synchronization
- **Unresolved core prerequisite gaps:** Probability/statistics is near-zero by self-report; this is expected and will be taught from first principles contextually rather than blocking Stage 0
- **Needs review:** Keep the terminology precise: dependency intent = broad requirements in `pyproject.toml`; resolution = exact graph in lockfile; sync = applying that resolution to an environment
- **Last updated:** 2026-09-16

## Learner Baseline

### Assume Known

- Core Python programming.
- Basic linear algebra familiarity only.
- Basic calculus familiarity only.

### Do Not Assume

- Probability foundations.
- Statistics foundations.
- Advanced linear algebra/calculus.
- Optimization theory beyond explicitly taught material.
- Any ML concept merely because related mathematics has been seen before.

### Teaching Rule for Mathematics / Statistics

Teach mathematical and statistical prerequisites **inside the ML topic that needs them**, not as a detached math course.

Examples:

- Naive Bayes → conditional probability + Bayes' theorem.
- Logistic regression → sigmoid, likelihood/log-loss, derivatives/gradients as needed.
- Evaluation/experimentation → sampling, bootstrap, confidence intervals, hypothesis tests, p-values, Type I/II error, effect size, statistical power.
- PCA → variance/covariance, projection, eigenvectors/eigenvalues, SVD.
- Optimization topics → required derivative/gradient/convexity intuition at point of use.

If a supposedly "basic" linear-algebra/calculus concept is shaky when needed, teach/review it briefly and continue from the paused ML topic.

---

## Diagnostic Status

| Area | Status | Evidence / Notes |
|---|---|---|
| Core Python | ASSUMED SUFFICIENT | Do not reteach as a prerequisite course |
| NumPy/Pandas/scientific Python | BASIC | Stage 1 checkpoint; fill gaps rather than reteach core Python |
| SQL | BASIC | Simple queries only; Stage 2 will build ML-oriented SQL depth |
| ML fundamentals | EARLY BEGINNER | Prior exposure to linear regression and basic classification |
| Probability | NEAR-ZERO | Self-rated below 1/5; teach from first principles contextually |
| Statistics | NEAR-ZERO | Self-rated below 1/5; teach from first principles contextually |
| Linear algebra | BASIC | Extend contextually when needed |
| Calculus | BASIC | Extend contextually when needed |
| Linux/Git | BASIC | Strengthen through Stage 0 and project work |
| Docker | BASIC | Reinforce now; deeper production use in Stage 9+ |
| Cloud | BASIC / LIGHT AWS | Small prior AWS exposure; formal cloud work later |
| Spark/Kafka/Kubernetes | NO ASSUMPTION | Curriculum teaches from first principles |

---

## Stage Learning Ledger

| Stage | Learning Status | Conceptual | Math/Stats | Coding | Applied Reasoning | Notes |
|---|---|---:|---:|---:|---:|---|
| 0 — Environment/Engineering Setup | LEARNING | Environment isolation understood | N/A | Conda environment creation/activation + interpreter verification demonstrated | Correctly explained dependency isolation and Git exclusion | Dependency declaration/locking is next |
| 1 — ML Python Ecosystem | NOT STARTED | — | — | — | — | |
| 2 — SQL/Data Handling | NOT STARTED | — | — | — | — | |
| 3 — Contextual Math/Probability/Stats Bridge | NOT STARTED | — | — | — | — | Integration checkpoint, not standalone math course |
| 4 — EDA/Preprocessing | NOT STARTED | — | — | — | — | |
| 4b — Evaluation Foundations | NOT STARTED | — | — | — | — | |
| 5 — Core Supervised ML | NOT STARTED | — | — | — | — | |
| 6 — Evaluation/Validation/Statistical Inference | NOT STARTED | — | — | — | — | |
| 7 — Feature Engineering/Model Improvement | NOT STARTED | — | — | — | — | |
| 8 — Unsupervised/Specialized Classical ML | NOT STARTED | — | — | — | — | |
| 9 — Production ML/MLOps Foundations | NOT STARTED | — | — | — | — | |
| 10A — Serving/Inference Modes | NOT STARTED | — | — | — | — | |
| 10B — PySpark | NOT STARTED | — | — | — | — | |
| 10C — Kafka/Streaming | NOT STARTED | — | — | — | — | |
| 10D — Cloud | NOT STARTED | — | — | — | — | |
| 10E — Kubernetes | NOT STARTED | — | — | — | — | |
| 11 — Monitoring/Reliability/Continuous ML | NOT STARTED | — | — | — | — | |
| 12 — ML System Design | NOT STARTED | — | — | — | — | |
| 13 — Responsible/Professional ML | NOT STARTED | — | — | — | — | |
| 14 — Staff+ / Research Literacy / Technical Leadership | NOT STARTED | — | — | — | — | |

Use qualitative evidence in notes rather than turning scores into false precision.

---

## Open Prerequisite Gaps

None recorded yet. Add entries only when an actual gap is demonstrated.

### Gap Entry Template

```markdown
### GAP-XXX — <Concept>
- **Detected in:** Stage/topic
- **Why it blocks progress:**
- **Repair needed:**
- **Evidence required to close:**
- **Status:** OPEN | CLOSED
- **Closed on:**
```

---

## Misconception Log — Append Only

No misconceptions recorded yet.

Use:

```markdown
### YYYY-MM-DD — <Misconception>
- What I believed:
- Correct model:
- How it was tested/repaired:
- Recheck date/topic:
```

---

## Review Queue

No scheduled review items yet.

| Topic | Reason | Review Trigger/Date | Status |
|---|---|---|---|
| — | — | — | — |

---

## Topic / Mastery Notes — Append as Topics Close

For important topics, keep compact retention notes:

```markdown
### <Topic>
- Problem it solves:
- Core intuition:
- Key math/statistics:
- Assumptions:
- Failure mode:
- Implementation pattern:
- Evaluation concern:
- Engineering implication:
- Evidence/project where used:
```

---

## Exact Continuation Point

### Next Teaching Step

Introduce uv as a resolver/locking tool without letting it compete with the existing Conda-managed environment. Teach the difference between uv's full project mode (`uv.lock` + uv-managed `.venv`) and its pip-compatible compile/sync mode. For the current Conda workflow, use `uv pip compile pyproject.toml -o requirements.lock` and install/sync explicitly against the Conda interpreter.

### Practice Before/With Next Lesson

Install uv as a standalone tool, verify `uv --version`, generate an exact lock from the existing `pyproject.toml`, inspect the resolved file, then recreate/sync dependencies into the Conda environment using an explicit interpreter path.

---

## Session Checkpoint History — Append Only

### 2026-09-14 — Initialized

- Track 1 learning state created.
- No topic marked mastered without evidence.
- Math baseline recorded as basic linear algebra + basic calculus; probability/statistics not assumed.
- Next step set to the first-session diagnostic/setup flow.

### 2026-09-16 — Initial diagnostic + Stage 0 environment isolation checkpoint

- Diagnostic recorded: SQL basic; prior ML exposure limited to linear regression/basic classification; probability/statistics near-zero; NumPy/Pandas basic; Git/Linux basic; Docker basic; light AWS exposure; 10–15 study hours/week; ~1-year interview horizon.
- Learner demonstrated project-local Conda environment creation with `conda create -p .venv python`, activation via `conda activate ./.venv`, and interpreter verification via `which python`.
- Concept check passed for why virtual environments exist, why `.venv` is not dependency metadata, why explicit interpreter/package-manager binding matters, and why environments should not be committed.
- Nuance retained for review: `pyproject.toml` declares project requirements but does not by itself guarantee an exact resolved environment; lock/reproduction mechanics are the next topic.


### 2026-09-16 — Dependency metadata/locking concept checkpoint

- Active environment reported Python 3.14.7, NumPy 2.5.3, pip 26.2.1.
- Learner correctly explained direct vs. transitive dependencies, version-range drift, `pyproject.toml` as project dependency metadata, and lockfiles as exact resolved dependency graphs.
- Correction retained: transitive dependencies usually should not be manually declared, but they still must be resolved, locked, audited and can cause conflicts/security issues.
- Tooling nuance identified: full uv project mode normally manages a project `.venv`; because Conda already owns the current `.venv`, current lessons will use uv's pip-compatible resolver/sync interface against the Conda interpreter to avoid two environment managers controlling one directory.


### 2026-09-16 — Dependency intent/resolution/sync misconception repaired

- Learner initially described dependency intent as what is in the lockfile and resolution as syncing to the environment.
- Correct model:
  - dependency intent = project requirements/constraints declared in `pyproject.toml`;
  - dependency resolution = exact compatible versions selected and recorded in a lockfile;
  - synchronization = making the actual environment match that resolved state.
- Learner correctly identified Requests as the direct package and certifi/charset-normalizer/idna/urllib3 as transitive dependencies in the drift exercise.
- Learner correctly explained why the package-management tool itself is not a runtime application dependency.
- Dependency reproducibility concept checkpoint is complete; next Stage 0 teaching topic is professional project structure and notebook-to-module workflow.


### 2026-09-16 — Project-structure concept check passed; implementation evidence pending

- Learner correctly explained that notebooks are for exploration/experimentation and reusable stable logic should move into `src/`.
- Learner correctly distinguished `src/` as reusable implementation from `scripts/` as runnable entry points/workflows.
- Learner correctly identified duplicated preprocessing logic as a maintenance and consistency risk.
- Important nuance: notebooks are not inherently bad; the risk is keeping critical reusable/production logic only in notebooks or duplicating it across notebooks.
- Implementation evidence for the project-structure exercise (directory tree + script output) is still pending, so the milestone is not complete.
