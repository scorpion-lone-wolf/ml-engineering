# ML/DL Program Index and Linear Progression Contract

## Purpose

This file is the repo-level navigation and continuity contract for the two-track ML Engineer program. It prevents stage jumping, parallel-track drift, and conflicting chat instructions.

## Authoritative Global Order

```text
TRACK 1 — CLASSICAL ML + PRODUCTION/MLOPS

ML Stage 0
→ Stage 1
→ Stage 2
→ Stage 3
→ Stage 4
→ Stage 4b Evaluation Foundations
→ Stage 5
→ Stage 6
→ Stage 7
→ Stage 8
→ Stage 9
→ Stage 10A Serving
→ Stage 10B PySpark
→ Stage 10C Kafka
→ Stage 10D Cloud
→ Stage 10E Kubernetes
→ Stage 11
→ Stage 12
→ Stage 13
→ Track 1 portfolio / readiness gate
→ TRACK 1 COMPLETE

ONLY THEN

TRACK 2 — DEEP LEARNING

DL-0 Track-1 gate/prerequisite bridge
→ DL-1 Neural-network foundations
→ DL-1a PyTorch foundations
→ DL-1b ML strategy
→ DL-2 Computer vision
→ DL-2b CV interpretability
→ DL-3 NLP / sequence modeling / Transformers
→ DL-3b DL forecasting
→ DL-4 Modern LLM architecture + alignment prerequisite bridge
→ DL-5 Production DL
→ DL-6 Generative-model architecture theory
→ Track 2 portfolio / readiness gate
→ PROGRAM COMPLETE
```

No later stage becomes active before its prerequisite stage is complete. A temporary backward branch is allowed only to repair a prerequisite gap, after which learning returns to the exact paused point.

## Canonical Repository Layout

```text
repo/
├── README.md
├── docs/
│   ├── PROGRAM_INDEX.md
│   ├── PROGRAM_STATUS.md
│   └── DECISIONS.md
├── ML/
│   ├── ML_CURRICULUM.md
│   └── docs/
│       ├── ML_MILESTONE_STATUS.md
│       └── ML_LEARNING_STATE.md
└── DL/
    ├── DL_CURRICULUM.md
    └── docs/
        ├── DL_MILESTONE_STATUS.md
        └── DL_LEARNING_STATE.md
```

## Source-of-Truth Hierarchy

- **Global track order/gate:** `PROGRAM_INDEX.md` → `PROGRAM_STATUS.md`.
- **Curriculum topics and stage order:** active track curriculum file.
- **Actual implementation/project state:** current repository → active track milestone-status file.
- **Learner understanding:** active track learning-state file.
- **Durable shared choices:** `DECISIONS.md`.
- **Chat/conversation memory:** useful context only; lowest authority when persistent files are available.

## First-Ever Session vs. Resume Session

- Use a curriculum's **First Response Instructions only for that track's first-ever session**.
- For every later session, use the track's **Start-of-Session Protocol**.
- A new ChatGPT conversation is not a new curriculum start.

## Required Startup Read Order

### While Track 1 is active
1. `docs/PROGRAM_INDEX.md`
2. `docs/PROGRAM_STATUS.md`
3. relevant section of `ML/ML_CURRICULUM.md`
4. `ML/docs/ML_LEARNING_STATE.md`
5. `ML/docs/ML_MILESTONE_STATUS.md`
6. relevant `docs/DECISIONS.md` entries
7. current project/repository files when implementation details matter

### While Track 2 is active
1. `docs/PROGRAM_INDEX.md`
2. `docs/PROGRAM_STATUS.md`
3. `ML/docs/ML_MILESTONE_STATUS.md` to verify the completed Track-1 gate
4. relevant section of `DL/DL_CURRICULUM.md`
5. `DL/docs/DL_LEARNING_STATE.md`
6. `DL/docs/DL_MILESTONE_STATUS.md`
7. relevant `docs/DECISIONS.md` entries
8. current project/repository files when implementation details matter

## Preservation Rule

Curriculum cleanup must never silently remove learning scope. Reordering, splitting into prerequisite sub-stages, deduplicating instruction text, and clarifying ownership between ML and DL are allowed; every meaningful ML/DL topic must remain represented unless the learner explicitly authorizes removal.
