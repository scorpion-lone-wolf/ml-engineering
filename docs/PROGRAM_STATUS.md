# PROGRAM STATUS — Global Track Gate

> This is the compact global resume point. Keep it current at the end of meaningful sessions.

## Current Snapshot

- **Program state:** ACTIVE
- **Active track:** Track 1 — Classical ML + Production ML/MLOps
- **Track 1 state:** ACTIVE
- **Track 2 state:** LOCKED
- **Current Track 1 stage:** Stage 0 — Environment and Engineering Setup
- **Current sub-stage/topic:** Reproducibility checkpoint
- **Last verified completed item:** Stage 0 clean-code refactor verified in repository
- **Blocking prerequisite gap:** None blocking Stage 0. Probability/statistics baseline is near-zero and will be taught contextually in later stages as designed.
- **Initialized:** 2026-09-14

## Exact Global Next Action

Continue **Track 1 Stage 0** with the reproducibility checkpoint. Do not begin Deep Learning.

## Exact Next Teaching Step

Teach reproducibility from first principles: identify the code, dependencies, configuration, inputs, and execution steps required for another run to reproduce the same behavior.

## Exact Next Practice / Engineering Step

Complete the reproducibility checkpoint, then README/setup workflow and the final Stage 0 reusable-project/mastery gate.

---

## Track Gate Table

| Track | State | Entry Requirement | Exit Requirement |
|---|---|---|---|
| Track 1 — Classical ML + Production | ACTIVE | Program start | All Track 1 stages/projects/readiness criteria passed with evidence |
| Track 2 — Deep Learning | LOCKED | Track 1 explicitly `COMPLETE` + final readiness gate passed | All DL stages/projects/readiness criteria passed with evidence |

## Track 1 → Track 2 Unlock Checklist

All must be true before changing Track 2 to `ACTIVE`:

- [ ] Every required Track 1 stage/sub-stage completion gate passed
- [ ] Required Track 1 portfolio work completed to the curriculum quality bar
- [ ] Classical ML/statistics/experimentation readiness demonstrated
- [ ] Production/MLOps/scale/reliability readiness demonstrated
- [ ] ML system-design readiness demonstrated
- [ ] Research-literacy / Staff+ Track 1 gate demonstrated
- [ ] `ML/docs/ML_LEARNING_STATE.md` has no unresolved core prerequisite gap
- [ ] `ML/docs/ML_MILESTONE_STATUS.md` marks final Track 1 readiness `COMPLETE`
- [ ] Track 1 completion recorded in the history below

---

## Status History — Append Only

### 2026-09-14 — Program initialized

- Track 1 set to `ACTIVE — INITIAL SETUP`.
- Track 2 set to `LOCKED`.
- No learning or implementation milestones were fabricated as complete.
- Initial next action: first-ever Track 1 diagnostic/setup flow.

### 2026-09-16 — Initial diagnostic completed; Stage 0 environment isolation demonstrated

- Learner baseline recorded across SQL, ML exposure, probability/statistics, NumPy/Pandas, Git/Linux, Docker, AWS, study capacity, and interview horizon.
- Stage 0 moved from initial setup to active learning.
- Project-local Conda environment creation/activation and interpreter verification demonstrated.
- ADR-001 records Conda as the local environment/interpreter manager, with pip fundamentals taught before uv is introduced.
- Exact next topic: dependency declaration and reproducibility with `pyproject.toml` and lockfiles.


### 2026-09-16 — Stage 0 project structure implementation verified

- Verified the pushed `ML/exercises/stage_00_project_structure/` exercise in the repository.
- Reusable package/module code and runnable script are present and match the earlier successful terminal output.
- Packaging/project-structure internals remain in the learner review queue; implementation is accepted without falsely marking conceptual mastery.
- Exact next topic: configuration vs. environment variables vs. secrets.


### 2026-09-19 — Configuration, logging, and testing checkpoint verified

- Implemented environment-driven log level and validated batch-size configuration with defaults, type conversion, positive-value validation, and fail-fast errors.
- Implemented Python logging with runtime log-level filtering, module logger usage, correct WARNING vs. ERROR branching, and avoidance of logging secrets.
- Added pytest as a development dependency and verified unit tests for cleaning behavior, boundary cases, environment-driven configuration, expected exceptions, monkeypatch isolation, and parameterized non-positive values.
- Testing nuance retained: a failed assertion proves actual behavior differs from the test expectation; the defect can be in application code, test expectation, or test setup.
- Stage 0 remains ACTIVE. Exact next topic: debugging fundamentals.


### 2026-09-19 — Debugging fundamentals learning checkpoint completed

- Learner practiced the debugging loop: define expected vs. actual behavior, reproduce, isolate, inspect relevant state, form a hypothesis, test the hypothesis, make a minimal fix, and verify.
- Learner correctly distinguished a hypothesis from an inspection technique after correction and applied the process to arithmetic and Stage 0 configuration examples.
- Reinforced that the crash/error location is not always the root-cause location, and that silent fallback can be more dangerous than a clear failure for invalid explicit configuration.
- No new implementation artifact was created for this checkpoint, so no implementation evidence was fabricated.
- Stage 0 remains ACTIVE. Exact next topic: Git/GitHub workflow and `.gitignore` checkpoint.


### 2026-09-20 — Git/GitHub and `.gitignore` checkpoint completed

- Learner correctly explained working tree/unstaged state, staging/index after `git add`, local commits, and remote publication via `git push`.
- Learner correctly explained that `.gitignore` applies to intentionally untracked files and does not retroactively remove already-tracked files from history.
- Learner correctly identified that an already-committed/pushed secret must be treated as exposed and rotated/revoked; history cleanup may also be required.
- Repository root `.gitignore` already contains Stage 0-relevant exclusions including `.venv/`, `.env`, `__pycache__/`, `.pytest_cache/`, coverage/build artifacts, and generated Python files.
- Learner reported the practical `git status` / `git check-ignore -v` verification succeeded; command output was not independently captured in chat.
- Stage 0 remains ACTIVE. Exact next topic: basic Linux/CLI checkpoint.


### 2026-09-20 — Basic Linux/CLI conceptual checkpoint completed

- Learner correctly explained parent-directory navigation with `cd ..`, copy vs. move semantics, overwrite vs. append redirection, and stdout-to-stdin piping.
- Covered `pwd`, `cd`, `ls`, `mkdir`, `rm`, `cp`, `mv`, `cat`, `less`, `which`, environment variables, stdin/stdout/stderr, pipes, and output redirection.
- Corrected terminology: `|` is a pipe, not pip; it connects stdout from the left command to stdin of the right command.
- No new repository artifact was created for this conceptual checkpoint.
- Stage 0 remains ACTIVE. Exact next topic: Python packaging mental-model review.


### 2026-09-20 — Python packaging mental-model review completed

- Learner correctly distinguished `.venv/` as the Python environment from `src/` as the source-layout directory and `ml_stage0/` as the importable package.
- Learner correctly identified `config.py` as a module and explained why a src-layout package may not be importable until the environment is configured through installation.
- Learner correctly explained `python -m pip install -e .`: use pip from the selected Python, install the current project in editable/development mode, read project/build metadata from `pyproject.toml`, and make the development source importable.
- Important refinement retained: editable mode is still an installation; the exact mechanism is build-backend dependent and should not be memorized simply as “a symlink.”
- Ordinary Python source edits are reflected without reinstalling after an editable install; packaging metadata or compiled-extension changes can require reinstall/rebuild.
- Packaging/src-layout/editable-install review item is now closed.
- Stage 0 remains ACTIVE. Exact next topic: clean-code fundamentals.


### 2026-09-21 — Clean-code checkpoint completed

- Verified pushed commit `3f8999af2dce00c8e55e42311aa00ff2f20b2070` in the repository.
- `src/ml_stage0/config.py` now preserves the original integer-conversion exception as the cause of the clearer configuration error using `raise ... from exc`.
- `scripts/demo_cleaning.py` now has an explicit `main() -> None` application entry point guarded by `if __name__ == "__main__":`.
- Learner demonstrated clean-code reasoning around focused responsibilities, accurate naming, avoiding duplicated preprocessing logic, mutation awareness, useful type hints, and avoiding premature abstraction.
- Repository contents were independently verified; local test execution was not independently observed in this checkpoint.
- Stage 0 remains ACTIVE. Exact next topic: reproducibility checkpoint.
