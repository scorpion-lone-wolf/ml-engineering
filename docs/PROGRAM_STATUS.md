# PROGRAM STATUS — Global Track Gate

> This is the compact global resume point. Keep it current at the end of meaningful sessions.

## Current Snapshot

- **Program state:** ACTIVE
- **Active track:** Track 1 — Classical ML + Production ML/MLOps
- **Track 1 state:** ACTIVE
- **Track 2 state:** LOCKED
- **Current Track 1 stage:** Stage 0 — Environment and Engineering Setup
- **Current sub-stage/topic:** Professional ML project structure and notebook-to-module workflow
- **Last verified completed item:** Stage 0 environment isolation + dependency declaration/locking/synchronization checkpoint
- **Blocking prerequisite gap:** None blocking Stage 0. Probability/statistics baseline is near-zero and will be taught contextually in later stages as designed.
- **Initialized:** 2026-09-14

## Exact Global Next Action

Continue **Track 1 Stage 0** with the professional ML project structure and the notebook → reusable module/script transition. Do not begin Deep Learning.

## Exact Next Teaching Step

Teach why ML work commonly starts in notebooks but production-quality logic must move into importable/testable modules and scripts. Build the minimal professional project skeleton and explain each directory by responsibility rather than memorization.

## Exact Next Practice / Engineering Step

Create the Stage 0 professional project skeleton and extract one small exploratory transformation from notebook-style code into `src/` plus a runnable script. Then continue with configuration, logging, testing, and README/setup workflow.

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
