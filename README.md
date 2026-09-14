# Machine Learning → Deep Learning Engineering Program

This repository is a long-running, evidence-based learning program for developing advanced Machine Learning Engineering and Deep Learning Engineering capability.

The program is deliberately broader and deeper than a typical course-completion roadmap. Its stretch target is the technical breadth, depth, engineering judgment, research literacy, production competence, and system-design ability associated with very strong Senior/Staff-level ML engineers. A job title or percentile is **not** granted by curriculum completion alone; those require sustained real-world impact and repeated evidence.

## Program Order

The program has two strictly ordered tracks:

1. **Track 1 — Classical ML + Production ML/MLOps**: `ML/ML_CURRICULUM.md`
2. **Track 2 — Deep Learning**: `DL/DL_CURRICULUM.md`

Track 2 remains **LOCKED** until Track 1 passes its final readiness gate.

## Repository Structure

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

## Learner Math Baseline

The mentor must use these assumptions unless later evidence updates them:

- Python: already known well enough to begin ML-specific work.
- Linear algebra: **basic familiarity only**.
- Calculus: **basic familiarity only**.
- Probability: **do not assume prior mastery**.
- Statistics: **do not assume prior mastery**.
- More advanced mathematics must be taught **just in time**, inside the ML/DL topic that needs it.
- Do **not** create a detached mathematics prerequisite course.
- Do **not** turn required mathematics into a black box.

Examples: teach Bayes' theorem when Naive Bayes requires it; likelihood when a modeling topic requires it; confidence intervals and hypothesis testing when evaluation/experimentation requires them; eigenvectors/SVD when PCA requires them; and chain rule/backprop math when neural networks require them.

## Starting a New Chat / Mentor Session

Read, in this order:

1. `docs/PROGRAM_INDEX.md`
2. `docs/PROGRAM_STATUS.md`
3. Curriculum for the currently active track
4. Active track's `*_LEARNING_STATE.md`
5. Active track's `*_MILESTONE_STATUS.md`
6. Relevant entries in `docs/DECISIONS.md`
7. Current repository/code when implementation state matters

Then resume from the **exact saved next action**. A new chat is never a reason to restart completed material.

## State vs. Curriculum

- Curriculum files define **what and in what order** to learn.
- Learning-state files record **what the learner demonstrably understands**.
- Milestone-status files record **what has actually been built/practiced/passed**.
- `PROGRAM_STATUS.md` controls the global Track 1 → Track 2 gate.
- `DECISIONS.md` stores durable choices so they are not repeatedly re-litigated.

## Core Rule

**Understanding before speed. Fundamentals before abstractions. Evidence before labels. Production reasoning before portfolio polish.**