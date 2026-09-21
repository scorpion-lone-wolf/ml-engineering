# ML LEARNING STATE — Demonstrated Understanding

> Track 1 learner-understanding source of truth. Update the current snapshot as learning progresses; preserve checkpoint/history sections.

## Current Snapshot

- **Track:** Track 1 — Classical ML + Production ML/MLOps
- **State:** LEARNING
- **Current stage:** Stage 0 — Environment and Engineering Setup
- **Current topic:** Reproducibility checkpoint
- **Last mastered topic:** Stage 0 clean-code fundamentals
- **Unresolved core prerequisite gaps:** Probability/statistics is near-zero by self-report; this is expected and will be taught from first principles contextually rather than blocking Stage 0
- **Needs review:** None currently blocking Stage 0
- **Last updated:** 2026-09-21

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

## Teaching Interaction Contract

- From this point onward, teach each section step by step without assuming unstated intermediate understanding.
- For each important conclusion, show the observable facts or inputs, the reasoning that connects them, and the resulting conclusion in simple language.
- Prefer jointly deriving the solution through small questions and examples before presenting the finished answer when the topic is instructional.
- Do not skip from a problem statement directly to a solution when the missing intermediate reasoning is part of what should be learned.
- When private/internal reasoning cannot be exposed, provide a concise user-facing rationale or derivation that is sufficient to understand why the step is valid.


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
| 0 — Environment/Engineering Setup | LEARNING | Environment/dependency, configuration, logging, testing, debugging, Git, Linux/CLI, packaging, and clean-code basics demonstrated | N/A | Conda env, lock workflow, src-layout package/script, validated env config, logging, pytest tests, Git/ignore workflow, and clean-code refactor demonstrated | Understands focused responsibilities, accurate naming, shared preprocessing, type-hint intent, mutation awareness, and explicit application entry points | Next: reproducibility checkpoint |
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
| Python packaging / src-layout / editable install | Practical workflow and mental model now demonstrated | Rechecked 2026-09-20 | CLOSED |

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


### Debugging Fundamentals
- **Problem it solves:** unexpected program behavior needs a repeatable way to locate the actual cause rather than changing code by guesswork.
- **Core intuition:** start with precise expected vs. actual behavior, reproduce the issue, isolate the smallest failing area, inspect only relevant state, form one hypothesis, test it, make the smallest justified change, and verify with tests or repeated execution.
- **Key concepts:** crash vs. wrong output vs. environment-dependent behavior; symptom vs. root cause; hypothesis vs. inspection; intermediate-state inspection; clear exceptions as debugging aids; silent fallback as a production risk.
- **Common failure modes:** changing code before reproducing the bug; confusing an inspection method with a hypothesis; assuming the line that crashes is always the root cause; hiding invalid configuration by silently falling back.
- **Implementation pattern:** use tests/logging/temporary inspection to gather evidence, then verify the minimal fix with the relevant test suite.
- **Engineering implication:** disciplined debugging reduces search space, avoids accidental fixes, and makes ML/data pipeline failures easier to trace back to preprocessing, configuration, or environment causes.
- **Evidence/project where used:** Stage 0 debugging exercises based on `clean_age()`, arithmetic examples, and `get_batch_size()`; conceptual checkpoint completed 2026-09-19 without fabricating a new code artifact.


### Git/GitHub Workflow and `.gitignore`
- **Problem it solves:** source changes need controlled local history, intentional commit boundaries, safe collaboration, and protection from accidentally tracking generated/local/sensitive files.
- **Core intuition:** edits live in the working tree; `git add` stages a selected snapshot in the index; `git commit` records staged content locally; `git push` publishes commits to a remote such as GitHub.
- **Key concepts:** working tree vs. staging/index vs. local repository vs. remote; tracked vs. untracked; focused commits; branch/PR mental model; `.gitignore` patterns; already-tracked-file caveat; secret rotation after exposure.
- **Common failure modes:** blindly staging everything; assuming `git commit` sends changes to GitHub; assuming `.gitignore` erases already-tracked history; treating a committed secret as safe after merely deleting the file.
- **Implementation pattern:** inspect with `git status`; stage intentional changes with `git add`; commit one coherent change; push to remote; use `git check-ignore -v` when diagnosing ignore behavior.
- **Engineering implication:** clean repository history and correct ignore rules improve reproducibility, reviewability, and security.
- **Evidence/project where used:** current repository root `.gitignore` plus ongoing Stage 0 commit/push workflow; learner reported `git status` and ignore checks succeeded on 2026-09-20.


### Clean-Code Fundamentals
- **Problem it solves:** code can work correctly but still be difficult to understand, test, modify, and debug if responsibilities and intent are mixed together.
- **Core intuition:** prefer focused responsibilities, names that describe actual behavior, shared implementations for rules that must stay consistent, useful type hints, and simple structure over unnecessary abstraction.
- **Key concepts:** responsibility separation; cleaning vs. validation terminology; mutation and side effects; duplicated preprocessing and training-serving skew; type hints as developer/tooling contracts rather than runtime enforcement; explicit `main()` entry points.
- **Common failure modes:** functions mixing data logic, terminal output, and file I/O; vague names such as `process_*`; duplicated training/prediction preprocessing; unused exception variables; executing workflows at import time; premature abstraction.
- **Implementation pattern:** keep reusable data/config logic in package modules and orchestration in an explicit script entry point; preserve exception causes when wrapping errors.
- **Engineering implication:** clearer boundaries reduce regression risk and help keep training and inference behavior aligned.
- **Evidence/project where used:** repository commit `3f8999af2dce00c8e55e42311aa00ff2f20b2070`; verified `config.py` exception chaining and `demo_cleaning.py` `main()` refactor on 2026-09-21.


## Exact Continuation Point

### Next Teaching Step

Teach the **reproducibility checkpoint** from first principles: define what must be fixed or recorded so another person or machine can reproduce a run—code version, Python/dependencies, configuration, inputs, and exact execution steps.

### Practice Before/With Next Lesson

Build the reproducibility model step by step using the current Stage 0 project, then identify what the repository already captures and what the README/setup workflow still needs to document.

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


### 2026-09-19 — Debugging fundamentals checkpoint

- Learner correctly identified expected vs. actual behavior in multiple examples and improved from suggesting inspection directly to stating an explicit causal hypothesis first.
- Practiced distinguishing reproduction (show the behavior consistently) from inspection (observe the state that can confirm or reject a hypothesis).
- Applied the workflow to boundary validation and invalid environment configuration; recognized the relevant `try/except` block as the isolated area when invalid input was silently defaulted.
- Reinforced that a clear fail-fast error is often safer than silently accepting an invalid explicit production configuration.
- No new code artifact was created for this topic; learning evidence is conceptual/applied reasoning only.
- Exact next topic: Git/GitHub workflow and `.gitignore` checkpoint.


### 2026-09-20 — Git/GitHub and `.gitignore` checkpoint

- Learner correctly identified working-tree/unstaged state before `git add` and staging/index state after `git add` but before `git commit`.
- Learner correctly explained that `.gitignore` does not undo already-tracked history and that an already-pushed secret should be considered exposed and rotated/revoked.
- Root `.gitignore` was inspected and already covers the important Stage 0 local/generated/sensitive paths.
- Learner reported successful practical verification with `git status` and `git check-ignore -v`; raw output was not pasted, so this is recorded as learner-reported practical evidence rather than independently captured terminal evidence.
- Exact next topic: basic Linux/CLI checkpoint.


### 2026-09-20 — Basic Linux/CLI checkpoint

- Learner correctly reasoned about `cd ..`, copy vs. move, overwrite vs. append redirection, and how a pipe connects stdout from one command to stdin of another.
- Core shell concepts covered: working directory, relative paths, file operations, executable lookup, environment variables, standard streams, pipes, and redirection.
- No new code artifact was created; this is recorded as conceptual/applied reasoning evidence.
- Exact next topic: Python packaging mental-model review.


### 2026-09-20 — Python packaging mental-model checkpoint

- Learner correctly separated `.venv/` (environment/runtime + installed packages), `src/` (source-layout directory), `ml_stage0/` (importable package), and `config.py` (module).
- Learner correctly explained why `import ml_stage0` can fail before installation in a src-layout project because Python does not automatically search arbitrary nested source directories.
- Learner correctly explained `python -m pip install -e .` as an editable installation of the current project using pip associated with the selected Python interpreter.
- Refinement retained: editable install is still an installation; its concrete mechanism varies by backend and should not be reduced to “it just creates a symlink.”
- Learner correctly explained why ordinary source edits are immediately reflected after editable installation.
- Packaging review queue item closed. Exact next topic: clean-code fundamentals.


### 2026-09-21 — Clean-code fundamentals checkpoint

- Learner correctly separated cleaning logic, terminal output, and file-writing responsibilities in a mixed-responsibility example.
- Learner correctly preferred a shared `clean_age` implementation over duplicated training/prediction preprocessing and understood the risk of inconsistent preprocessing behavior.
- Learner correctly interpreted `list[str]` as a type contract for readers/tooling while recognizing Python does not enforce it automatically at runtime.
- Learner understood why `clean_users` is more accurate than `validate_users` when the function actually transforms invalid values.
- Verified pushed refactor: exception chaining in `config.py` and explicit `main()` entry point in `demo_cleaning.py`.
- Teaching preference recorded: derive future material step by step, make intermediate rationale explicit, and avoid assumed jumps.
- Exact next topic: reproducibility checkpoint.


### 2026-09-21 — Clean-code runtime verification

- Follow-up repository review confirmed the readability cleanup from `x` to `cleaned_age` in the invalid-count comprehension.
- Learner-provided terminal evidence showed 9/9 pytest cases passing after the clean-code refactor.
- Learner-provided script output confirmed the application still executes successfully with the expected configuration logs, all-invalid error log, and cleaned result.
- This closes the clean-code checkpoint with both conceptual understanding and runtime verification.
- Exact next topic: reproducibility checkpoint.
