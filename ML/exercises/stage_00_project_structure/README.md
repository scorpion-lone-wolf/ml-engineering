# Stage 0 — Python Project Structure and Local Package Basics

## Topic

**From exploratory Python files to reusable project code**

This exercise demonstrates how reusable Python code can live in a package and be imported by scripts without copying the same function into multiple files.

## Why we did this

ML work often starts in notebooks or small scripts. Once logic becomes useful in more than one place—training, evaluation, inference, tests, or another notebook—it should move into reusable modules.

The goal is to avoid duplicated logic such as preprocessing code being copied into several notebooks or services and then drifting apart.

## Project structure used here

```text
stage_00_project_structure/
├── README.md
├── pyproject.toml
├── scripts/
│   └── demo_cleaning.py
└── src/
    └── ml_stage0/
        ├── __init__.py
        └── features/
            ├── __init__.py
            └── cleaning.py
```

### What each part means

- `src/` — ordinary directory used by convention to hold importable source code. It is **not** a Python keyword or reserved folder.
- `ml_stage0/` — the actual Python package that we import as `ml_stage0`.
- `features/` — a subpackage used here to group feature/preprocessing code.
- `cleaning.py` — a Python module.
- `clean_age` — a function inside that module.
- `scripts/demo_cleaning.py` — a runnable entry point that uses the reusable package code.
- `pyproject.toml` — project/package metadata and packaging configuration used by tools such as pip/setuptools.

## Import path used

```python
from ml_stage0.features.cleaning import clean_age
```

Read it from left to right:

```text
ml_stage0   -> package
features    -> subpackage
cleaning    -> module (cleaning.py)
clean_age   -> function
```

There is no `src.__init__.py` because `src` is not part of the import path. It is just the directory containing the real package.

## Why `pyproject.toml` exists

The file currently contains three kinds of information.

### 1. Project metadata

```toml
[project]
name = "ml-stage0"
version = "0.1.0"
description = "Stage 0 ML engineering project structure exercise"
requires-python = ">=3.11"
dependencies = []
```

This describes the project itself: its distribution name, version, supported Python version, and runtime dependencies.

### 2. Build backend

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"
```

This tells packaging tools that **setuptools** knows how to build/install this project.

### 3. Package location

```toml
[tool.setuptools.packages.find]
where = ["src"]
```

This tells setuptools to look under `src/` for Python packages. It then finds `src/ml_stage0/`.

## What `python -m pip install -e .` means

Break it into pieces:

- `python` — use the currently active Python interpreter.
- `-m pip` — run pip using that interpreter.
- `install` — install a package/project.
- `-e` — editable/development mode.
- `.` — the project in the **current directory**.

So the command means:

> Use my active Python environment, and install the Python project in the current directory in editable/development mode.

The project name does not need to appear in the command because pip reads it from `pyproject.toml`.

Editable mode is useful while developing because imports continue to use the local source tree. If `src/ml_stage0/features/cleaning.py` changes, the next run normally sees that source change without reinstalling after every edit.

## Environment vs source code

These are different concerns:

- `.venv/` answers: **Which Python interpreter and installed external packages am I using?**
- `src/` answers: **Where did this repository choose to store its importable source code?**
- `pyproject.toml` answers: **How is this Python project described/built/installed?**

They should not be treated as the same thing.

## Why this matters for ML engineering

The same preprocessing code may eventually be used by:

- training;
- evaluation;
- batch inference;
- an API;
- tests;
- notebooks.

Keeping the logic in one reusable module reduces training-serving skew and maintenance bugs.

## Exercise result

`demo_cleaning.py` imports `clean_age` from the package and produces:

```text
[25, None, 32, 40, None]
```

This proves the script can use the reusable package code rather than duplicating it.
