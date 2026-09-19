# ML LEARNING STATE — Demonstrated Understanding

> Track 1 learner-understanding source of truth. Update the current snapshot as learning progresses; preserve checkpoint/history sections.

## Current Snapshot

- **Track:** Track 1 — Classical ML + Production ML/MLOps
- **State:** LEARNING
- **Current stage:** Stage 0 — Environment and Engineering Setup
- **Current topic:** Debugging fundamentals
- **Last mastered topic:** Stage 0 configuration/environment variables/secrets, logging fundamentals, and core unit-testing fundamentals
- **Unresolved core prerequisite gaps:** Probability/statistics is near-zero by self-report; this is expected and will be taught from first principles contextually rather than blocking Stage 0
- **Needs review:** Python packaging mental model: `.venv` = runtime environment; `src/` = ordinary source-code layout directory; `ml_stage0/` = importable package; `pyproject.toml` = project/build/package configuration; editable install registers the local project for development
- **Last updated:** 2026-09-19

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
| 0 — Environment/Engineering Setup | LEARNING | Environment/dependency, configuration, logging, and testing basics demonstrated; package-layout concepts need reinforcement | N/A | Conda env, lock workflow, src-layout package/script, validated env config, logging, and pytest tests demonstrated | Understands fail-fast configuration, log severity/filtering, test boundaries, monkeypatch isolation, expected exceptions, and parameterization | Next: debugging fundamentals |
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

### 2026-09-19 — Interpreting a failing assertion
- What I believed: A failed assertion such as `assert get_batch_size() == 64` means the function is not working as expected.
- Correct model: A failed assertion only proves that actual behavior differs from the test expectation; the application code, the test expectation, or the test setup may be wrong.
- How it was tested/repaired: Earlier deliberate failure changed the expected value from 25 to 30 while leaving correct application code unchanged; pytest correctly failed the bad test.
- Recheck date/topic: Recheck during Stage 0 debugging fundamentals.


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

| Topic | Reason | Review Trigger/Date | Status |
|---|---|---|---|
| Python packaging / src-layout / editable install | Practical workflow works, but the mental model is not yet intuitive | Revisit when the next project/package import is created or before Stage 0 completion gate | OPEN |

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



### Python Project Structure and Local Package Basics
- **Problem it solves:** reusable ML logic should not be duplicated across notebooks, training scripts, inference code, and tests.
- **Core intuition:** keep reusable Python logic in modules/packages; keep runnable workflows in scripts; notebooks remain useful for exploration.
- **Key concepts:** `.venv/` is the Python runtime environment; `src/` is an ordinary source-layout directory, not a keyword; `ml_stage0/` is the actual importable package; `cleaning.py` is a module; `clean_age` is a function.
- **Why `pyproject.toml`:** it describes the Python project and tells packaging/build tools what the project is, which build backend to use, and—in this exercise—where package source lives.
- **Why editable install:** `python -m pip install -e .` means “using this Python, install the project in the current directory in editable/development mode”; it makes the local package importable while continuing to use the working source tree.
- **Common failure mode:** confusing the environment (`.venv`) with the source layout (`src`), or assuming `src` is a reserved Python directory. Another failure mode is copying preprocessing code into multiple notebooks/services and allowing the copies to drift.
- **Implementation pattern:** `src/ml_stage0/features/cleaning.py` provides reusable logic; `scripts/demo_cleaning.py` imports and executes it.
- **Engineering implication:** one shared preprocessing implementation reduces inconsistent training/inference behavior and makes later testing easier.
- **Evidence/project where used:** `ML/exercises/stage_00_project_structure/`; repository code verified on 2026-09-16. Concept is implemented, but packaging details remain scheduled for reinforcement rather than marked fully mastered.

---

### Configuration, Logging, and Core Unit Testing
- **Problem it solves:** external runtime values need safe validation, running applications need observable behavior, and important code behavior needs automated regression checks.
- **Core intuition:** treat environment values as untrusted strings at the configuration boundary; convert and validate early; use logs for operational events and `print` for intended program output; tests encode expected behavior and boundaries.
- **Key concepts:** code vs. configuration vs. secrets; environment-variable defaults; type/domain validation; fail-fast errors; DEBUG/INFO/WARNING/ERROR/CRITICAL; log filtering; unit tests; Arrange–Act–Assert; pytest discovery; fixtures; `monkeypatch`; `pytest.raises`; parameterization.
- **Common failure modes:** silently accepting invalid configuration; logging secrets; treating `print` as logging; emitting WARNING and ERROR for the same mutually-exclusive condition; assuming every failed test proves production code is wrong.
- **Implementation pattern:** `src/ml_stage0/config.py`, logging in `scripts/demo_cleaning.py`, tests under `tests/test_cleaning.py` and `tests/test_config.py`.
- **Engineering implication:** configuration errors fail near startup, operational behavior is observable, and regressions in cleaning/configuration behavior can be caught automatically.
- **Evidence/project where used:** `ML/exercises/stage_00_project_structure/`; repository code verified through 2026-09-19.


## Exact Continuation Point

### Next Teaching Step

Teach **debugging fundamentals** from first principles using a concrete broken Stage 0 example. Use the loop: reproduce → isolate → inspect state → form a hypothesis → test the hypothesis → verify the fix.

### Practice Before/With Next Lesson

Debug one intentionally broken example in the Stage 0 project. After that, continue the Git/Linux checkpoint, packaging mental-model review, clean-code/reproducibility review, and README/setup workflow before the Stage 0 completion gate.

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


### 2026-09-16 — Project-structure implementation verified in repository

- Verified `ML/exercises/stage_00_project_structure/pyproject.toml`.
- Verified reusable implementation at `src/ml_stage0/features/cleaning.py`.
- Verified package markers at `src/ml_stage0/__init__.py` and `src/ml_stage0/features/__init__.py`.
- Verified runnable entry point at `scripts/demo_cleaning.py`.
- Earlier terminal evidence showed successful editable installation and expected output.
- Learner requested that packaging/project-structure details remain as reference notes because the practical workflow worked but the packaging mental model is not yet fully intuitive.
- Decision: do not falsely mark packaging internals mastered; retain them in the review queue and move to the next Stage 0 topic, configuration/environment variables/secrets.


### 2026-09-19 — Configuration, logging, and testing fundamentals checkpoint

- Configuration concepts demonstrated: code vs. configuration vs. secrets, environment-provided values, defaults, string-to-int conversion, positive-value domain validation, and fail-fast errors.
- Logging concepts demonstrated: severity levels, threshold filtering, `logging.getLogger(__name__)`, parameterized log messages, print-vs-log distinction, secret-safety, and mutually-exclusive WARNING/ERROR conditions.
- Testing concepts demonstrated with pytest: discovery, Arrange–Act–Assert, happy path, negative/boundary cases, `monkeypatch` environment isolation, `pytest.raises`, and parameterized invalid inputs.
- Learner correctly explained why zero is a meaningful boundary, why tests must control environment state, and why parameterization reduces duplicated test code.
- Correction retained for debugging review: failed assertions indicate a mismatch between actual and expected behavior, not automatically a defect in application code.
- Packaging/src-layout/editable-install mental model remains in the review queue before the Stage 0 completion gate.
- Exact next topic: debugging fundamentals.
