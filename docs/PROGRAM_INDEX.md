# PROGRAM INDEX — Global Learning Contract

## 1. Purpose

This file is the global contract for the two-track ML Engineering program. It defines canonical paths, track order, learner assumptions, startup/update behavior, and source-of-truth rules.

It does **not** replace either curriculum.

---

## 2. Target

Develop broad and deep capability across:

- classical machine learning;
- probability/statistics used in ML;
- data work and experimentation;
- production ML/MLOps;
- distributed data/streaming/cloud systems;
- ML system design;
- deep learning across CV/NLP/representation/generative modeling;
- DL systems/performance;
- research reproduction and benchmarking;
- Staff+-style technical judgment, written design, review, and cross-team reasoning.

The stretch bar is intentionally above a normal "course complete" Senior MLE checklist. Completion is evidence of preparation, **not a guarantee of a Staff title or top-percentile standing**; real-world scope, impact, judgment, and collaboration still matter.

---

## 3. Strict Track Order

### Track 1 — ACTIVE FIRST

Canonical curriculum:

`ML/ML_CURRICULUM.md`

Covers classical ML, contextual probability/statistics/math, experimentation, production ML/MLOps, scale, reliability, system design, research literacy, and Staff+ engineering practice.

### Track 2 — LOCKED UNTIL TRACK 1 COMPLETES

Canonical curriculum:

`DL/DL_CURRICULUM.md`

Track 2 must not begin until Track 1 is explicitly marked `COMPLETE` in `docs/PROGRAM_STATUS.md` **and** Track 1's final readiness gate is satisfied with evidence.

No parallel Track 1/Track 2 progression.

---

## 4. Permanent Learner Baseline

Unless stronger evidence in a learning-state file supersedes it:

### Already Known / Assumed

- Core Python programming.
- Basic linear algebra familiarity: vectors, matrices, simple matrix operations at a basic level.
- Basic calculus familiarity: functions, derivatives, basic differentiation intuition.

### Do Not Assume

- Probability foundations.
- Statistics foundations.
- Advanced linear algebra.
- Advanced calculus.
- Optimization theory beyond what has been explicitly taught/verified.
- Any ML/DL topic merely because its prerequisite math has been encountered before.

### Contextual Math Rule

There is **no standalone mathematics course** in this program.

Whenever the active ML/DL topic needs mathematics:

1. name the exact prerequisite;
2. quickly verify existing understanding;
3. teach missing pieces at the depth needed for the current topic;
4. give intuition plus equations;
5. define symbols/shapes;
6. use a small worked numeric example;
7. connect the math to the algorithm/model behavior;
8. then implement/apply it.

Probability/statistics must follow the same rule. Examples include conditional probability, Bayes' theorem, random variables/distributions, expectation/variance, likelihood, sampling, confidence intervals, hypothesis testing, power, calibration, and experiment uncertainty.

---

## 5. Canonical Repository Map

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
│       ├── ML_LEARNING_STATE.md
│       └── ML_MILESTONE_STATUS.md
└── DL/
    ├── DL_CURRICULUM.md
    └── docs/
        ├── DL_LEARNING_STATE.md
        └── DL_MILESTONE_STATUS.md
```

### File Responsibilities

| File | Responsibility |
|---|---|
| `docs/PROGRAM_INDEX.md` | Global contract, canonical paths, read order, source hierarchy |
| `docs/PROGRAM_STATUS.md` | Global active-track gate and exact global continuation point |
| `docs/DECISIONS.md` | Append-only durable technical/program decisions |
| `ML/ML_CURRICULUM.md` | Authoritative Track 1 syllabus/order |
| `ML/docs/ML_LEARNING_STATE.md` | Demonstrated Track 1 understanding, gaps, review queue, exact next teaching step |
| `ML/docs/ML_MILESTONE_STATUS.md` | Track 1 implementation/practice/deliverable evidence, exact next work step |
| `DL/DL_CURRICULUM.md` | Authoritative Track 2 syllabus/order |
| `DL/docs/DL_LEARNING_STATE.md` | Demonstrated Track 2 understanding, gaps, review queue, exact next teaching step |
| `DL/docs/DL_MILESTONE_STATUS.md` | Track 2 implementation/practice/deliverable evidence, exact next work step |

---

## 6. Start-of-Session Read Order

### When Track 1 Is Active

1. `docs/PROGRAM_INDEX.md`
2. `docs/PROGRAM_STATUS.md`
3. relevant current section of `ML/ML_CURRICULUM.md`
4. `ML/docs/ML_LEARNING_STATE.md`
5. `ML/docs/ML_MILESTONE_STATUS.md`
6. relevant `docs/DECISIONS.md` entries
7. repository/code evidence when implementation matters

### When Track 2 Is Active

1. `docs/PROGRAM_INDEX.md`
2. `docs/PROGRAM_STATUS.md`
3. `ML/docs/ML_MILESTONE_STATUS.md` to verify the Track 1 gate
4. relevant current section of `DL/DL_CURRICULUM.md`
5. `DL/docs/DL_LEARNING_STATE.md`
6. `DL/docs/DL_MILESTONE_STATUS.md`
7. relevant `docs/DECISIONS.md` entries
8. repository/code evidence when implementation matters

After reading, briefly recover:

- active track;
- current stage/sub-stage;
- last completed item;
- unresolved prerequisite gaps;
- exact next teaching step;
- exact next practice/engineering step.

Then continue from that point.

---

## 7. End-of-Session Update Contract

When wrapping up or when asked to update state:

1. Update the active `*_LEARNING_STATE.md` snapshot.
2. Update the active `*_MILESTONE_STATUS.md` snapshot.
3. Preserve append-only history/checkpoint sections.
4. Update `docs/PROGRAM_STATUS.md` with the exact global continuation point.
5. Append to `docs/DECISIONS.md` only when a durable decision was actually made.
6. Record exact next teaching and engineering/practice actions.

Do not mark a stage complete merely because it was explained.

---

## 8. Completion Semantics

Allowed learning/milestone states:

- `NOT STARTED`
- `LEARNING`
- `PRACTICING`
- `NEEDS REVIEW`
- `MASTERED` / `COMPLETE` only when the corresponding gate is satisfied
- `LOCKED` for work whose prerequisite track/stage has not opened

A stage completes only when its curriculum completion gate is satisfied through exercises, explanation, implementation, debugging, and deliverables where required.

---

## 9. Source-of-Truth Hierarchy

When sources conflict:

1. **Global program order and canonical paths:** `docs/PROGRAM_INDEX.md`
2. **Global active track/gate:** `docs/PROGRAM_STATUS.md`
3. **Curriculum order:** relevant curriculum file
4. **Actual implementation/project state:** current repository/code → milestone-status file → chat recollection
5. **Demonstrated learner understanding:** learning-state file → chat assumptions
6. **Durable decisions:** `docs/DECISIONS.md`

Never unlock later work from chat memory alone.

---

## 10. Change Policy

Curriculum files are stable master specifications. Do not casually rewrite them because a chat changed.

State files are expected to evolve continuously.

`docs/DECISIONS.md` is append-only. If a decision changes, create a new entry and mark the old one `Superseded`; do not erase history.

---

## 11. Scope Boundary

This repository is for core ML/DL engineering. Do not let it drift into a generic GenAI/agent-application roadmap. LLM architecture is valid DL content; LangChain/RAG/agent-product development is a separate concern unless a separate track is explicitly created later.