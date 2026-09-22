# PROGRAM STATUS — Global Track Gate

> This is the compact global resume point. Keep it current at the end of meaningful sessions.

## Current Snapshot

- **Program state:** ACTIVE
- **Active track:** Track 1 — Classical ML + Production ML/MLOps
- **Track 1 state:** ACTIVE
- **Track 2 state:** LOCKED
- **Current Track 1 stage:** Stage 0 — Environment and Engineering Setup
- **Current sub-stage/topic:** Reproducibility checkpoint
- **Last verified completed item:** Stage 0 reproducibility dependency-lock/sync sub-checkpoint verified with committed `requirements.lock`, editable reinstall, 9/9 passing tests, and expected script execution
- **Blocking prerequisite gap:** None blocking Stage 0. Probability/statistics baseline is near-zero and will be taught contextually in later stages as designed.
- **Initialized:** 2026-09-14

## Exact Global Next Action

Continue **Track 1 Stage 0** with the reproducibility checkpoint. Do not begin Deep Learning.

## Exact Next Teaching Step

Continue reproducibility by documenting the exact tested Python 3.14.7 runtime separately from the restored `>=3.11` compatibility declaration, adding a safe configuration example, and completing the setup/run instructions needed for a clean recreation.

## Exact Next Practice / Engineering Step

Finish the reproducibility checkpoint: document Python 3.14.7 as the tested environment, add a committed `.env.example`, update stale README/setup/output instructions, and verify a clean recreation. Then run the final Stage 0 audit/mastery gate, including the remaining explicit IDE-workflow check.

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


### 2026-09-21 — Clean-code runtime verification completed

- Verified the follow-up cleanup commit on `master`: the invalid-count comprehension now uses the clearer `cleaned_age` variable name.
- Learner provided terminal evidence showing all 9 pytest cases passed after the refactor.
- Learner also provided runtime output showing INFO configuration logs, the expected all-invalid ERROR log, and the resulting cleaned list of `None` values.
- Clean-code checkpoint is fully complete with repository and runtime evidence.
- Exact next topic remains: reproducibility checkpoint.


### 2026-09-22 — Reproducibility dependency layer verified

- Learner derived the reproducibility model across code version, runtime, dependencies, configuration, inputs, and execution procedure.
- Generated and committed `ML/exercises/stage_00_project_structure/requirements.lock` using uv's pip-compatible compile workflow; the lock records pytest plus its transitive dependencies at exact resolved versions.
- Demonstrated `uv pip sync requirements.lock --dry-run`, correctly predicted that the editable local project would be removed because it is not part of the external dependency lock, then performed the actual sync.
- Reinstalled the current source checkout with `uv pip install -e .`; learner-provided runtime evidence then showed 9/9 pytest cases passing and the demo script producing the expected current output.
- Repository commit `60b6ab5c24f0913ffbe5a5812ccdad38b38de2da` is verified for the lockfile addition.
- Open correction: that commit also changed `requires-python` from the compatibility range `>=3.11` to `==3.14.7`. The exact tested runtime should be documented separately from project compatibility, so this must be corrected before the reproducibility checkpoint closes.
- `.env.example` is not yet present in the pushed repository; configuration documentation therefore remains open.
- Stage 0 remains ACTIVE. Exact next work: finish runtime/configuration/README reproducibility, verify clean recreation, then perform the final Stage 0 audit including IDE workflow.


### 2026-09-22 — Python compatibility declaration corrected

- Verified commit `50bb70d42a72859eae5e143d77ebc6156eadca5c` restoring `requires-python = ">=3.11"` in the Stage 0 project.
- This correctly separates project compatibility from the exact tested development runtime (Python 3.14.7), which still needs to be documented in the reproducible setup instructions.
- The committed dependency lock remains intact.
- `.env.example` and the README/setup refresh are not yet present, so the reproducibility checkpoint remains open.
