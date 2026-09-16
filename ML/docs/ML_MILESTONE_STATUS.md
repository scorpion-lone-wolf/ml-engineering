# ML MILESTONE STATUS — Implementation, Practice and Deliverables

> Track 1 evidence-of-work source of truth. A concept being explained does not complete a milestone.

## Current Snapshot

- **Track state:** ACTIVE
- **Current stage:** Stage 0 — Environment and Engineering Setup
- **Current implementation milestone:** Environment isolation and dependency declaration concepts demonstrated; exact locking workflow next
- **Current project:** Stage 0 reusable professional ML project template
- **Last verified completed deliverable:** Stage 0 environment + dependency metadata concept checkpoints
- **Exact next work step:** Install uv, generate an exact dependency lock from `pyproject.toml` using uv's pip-compatible workflow, and sync explicitly to the Conda interpreter
- **Last updated:** 2026-09-16

---

## Stage / Sub-stage Milestones

| Stage | Status | Required Evidence / Deliverable | Evidence Location |
|---|---|---|---|
| 0 — Environment and Engineering Setup | LEARNING | Reusable professional ML project template; environment/reproducibility/testing workflow demonstrated | `ML/exercises/stage_00_environment/` environment exercise (local evidence reported in session) |
| 1 — ML Python Ecosystem Checkpoint | NOT STARTED | Gap-focused scientific-Python/data tasks; messy-data mini work | — |
| 2 — SQL and Data Handling | NOT STARTED | Correct ML-oriented SQL tasks including point-in-time/leakage reasoning | — |
| 3 — Contextual Math/Probability/Stats Bridge | NOT STARTED | Integration checkpoint demonstrating prerequisites needed for upcoming algorithms | — |
| 4 — EDA and Preprocessing | NOT STARTED | Data-quality report + leakage-safe preprocessing pipeline | — |
| 4b — Evaluation Foundations | NOT STARTED | Correct split + trivial baseline + justified metric | — |
| 5 — Core Supervised ML | NOT STARTED | Algorithm exercises, selected from-scratch implementations, sklearn application/debugging | — |
| 6 — Evaluation/Validation/Statistical Inference | NOT STARTED | Rigorous validation + uncertainty/statistical experiment analysis + metric/threshold reasoning | — |
| 7 — Feature Engineering/Model Improvement | NOT STARTED | Reproducible feature pipeline + model-diagnosis/improvement evidence | — |
| 8 — Unsupervised/Specialized Classical ML | NOT STARTED | Clustering/PCA/anomaly/recsys/NLP/retrieval/time-series/RL-foundation applied work as required | — |
| 9 — Production ML/MLOps Foundations | NOT STARTED | Reproducible train/package/register/serve/test/container/CI-CD workflow | — |
| 10A — Model Serving/Inference Modes | NOT STARTED | Batch/online/asynchronous/streaming inference reasoning and implementation exercises | — |
| 10B — PySpark | NOT STARTED | Rebuild an earlier feature pipeline in PySpark + explain scale trade-offs | — |
| 10C — Kafka/Streaming | NOT STARTED | Minimal producer/consumer → rolling feature computation → inference endpoint | — |
| 10D — Cloud | NOT STARTED | Deploy/map core ML building blocks on one primary cloud with security/cost reasoning | — |
| 10E — Kubernetes | NOT STARTED | Deploy/scale an ML inference service using minimum relevant K8s primitives | — |
| 11 — Monitoring/Reliability/Continuous ML | NOT STARTED | Monitoring + drift/retraining exercise with reliability reasoning | — |
| 12 — ML System Design | NOT STARTED | Multiple end-to-end design exercises + trade-off reviews | — |
| 13 — Responsible/Professional ML | NOT STARTED | Governance/security/privacy/fairness/documentation/professional-engineering evidence | — |
| 14 — Staff+ / Research / Technical Leadership | NOT STARTED | Paper/result reproduction, ablation/benchmark, technical RFC/review/incident-style exercises | — |

---

## Portfolio-Grade Track 1 Systems

| Project | Status | Minimum Purpose |
|---|---|---|
| Project A — Tabular Risk/Fraud/Churn System | NOT STARTED | End-to-end imbalanced tabular production ML |
| Project B — Recommendation/Ranking System | NOT STARTED | Candidate generation/ranking/cold-start/evaluation/serving |
| Project C — Time-Series Forecasting System | NOT STARTED | Backtesting, feature pipelines, forecast service/job, monitoring |
| Project F — ML Platform / Reusable Training Pipeline | NOT STARTED | Configurable reproducible training/registry/validation/deployment/monitoring |

Projects may be combined only when the resulting artifact genuinely demonstrates the required competencies.

---

## Evidence Registry

Add evidence instead of writing "done" without proof.

| Evidence ID | Stage/Project | Type | Repository/File/PR | What It Proves | Verified? |
|---|---|---|---|---|---|
| — | — | — | — | No evidence recorded yet | — |

Evidence can include code, tests, experiment reports, design docs, benchmark reports, deployment manifests, dashboards, postmortems, project retrospectives, and mastery-review notes.

---

## Active Work

Stage 0 environment-isolation practice has started. The learner created a project-local Conda environment and verified the active interpreter path.

### Exact Next Engineering / Practice Step

In `ML/exercises/stage_00_environment/`, keep Conda responsible for the environment/interpreter, install uv as a standalone tool, generate an exact lock with `uv pip compile pyproject.toml -o requirements.lock`, inspect the resolved dependency graph, and use an explicit Conda interpreter when syncing/installing. Then continue the reusable project-template deliverable with configuration, logging, tests, and README/setup instructions.

---

## Track 1 Final Readiness Gate

Do not mark `COMPLETE` until all are evidenced:

- [ ] Classical ML fundamentals and contextual mathematics
- [ ] Probability/statistics/inference/experimentation competency
- [ ] Correct modeling/evaluation/error-analysis workflow
- [ ] SQL/data/feature correctness including temporal leakage and point-in-time reasoning
- [ ] Production lifecycle: packaging, serving, containers, CI/CD, registry/versioning
- [ ] Spark/Kafka/cloud/Kubernetes scale fundamentals
- [ ] Monitoring/reliability/retraining/rollback reasoning
- [ ] ML system design across several representative systems
- [ ] Responsible/professional ML engineering
- [ ] Research reproduction + ablation/benchmark discipline
- [ ] Staff+-style RFC/design-review/incident/technical-strategy exercises
- [ ] Portfolio artifacts meet stated quality bar
- [ ] Interview readiness demonstrated
- [ ] No unresolved core prerequisite gap in `ML_LEARNING_STATE.md`

---

## Completion / Milestone History — Append Only

### 2026-09-14 — Initialized

- No stage or project marked complete without evidence.
- Track 1 positioned at Stage 0 initial setup.

### 2026-09-16 — Stage 0 environment isolation checkpoint

- Initial diagnostic completed.
- Project-local Conda environment workflow demonstrated.
- Interpreter switched from Anaconda base (`/opt/anaconda3/bin/python`) to the exercise environment after activation.
- Learner correctly explained isolation, Git exclusion, and the role difference between an environment and dependency metadata.
- Stage 0 remains in progress; dependency declaration/locking and the reusable project-template deliverable are not yet complete.


### 2026-09-16 — Dependency declaration checkpoint

- `pyproject.toml` dependency intent vs. exact lockfile state understood.
- Direct vs. transitive dependency distinction explained correctly.
- Current exercise environment: Python 3.14.7, NumPy 2.5.3, pip 26.2.1.
- No transitive dependency chain is visible yet because the tiny environment only contains NumPy and pip.
- Next evidence: produce and inspect an exact lock and reproduce/sync the environment from it.
