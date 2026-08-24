# AGENTS.md

Guidance for AI agents (and humans) working in this repo.

## What this repo is
E-learning coursework and tutorials: Coursera courses (Stanford ML, Deep
Learning Specialization, TensorFlow intro, Data-Driven Astronomy),
HackerRank exercises, and short Python / T-SQL tutorials. Mostly Jupyter
notebooks plus some MATLAB, Python, and SQL. Projects are fully standalone.

## Naming
- One top-level folder per course/tutorial, named `snake_case`
  (e.g. `python`). No spaces, no CamelCase.
  (Subfolders inside a course keep their original course structure.)
- Every top-level course folder should have a short `README.md`:
  what the course is and how to work through it.

## Python environments
- **One `.venv` per course folder, created on demand.** Never a shared env —
  courses pin conflicting versions across eras.
- **Dependency standard: `pyproject.toml` + `uv.lock` per course folder**
  (only where Python deps exist beyond the standard library):
  - `pyproject.toml` declares dependencies (PEP 621 `[project]` table).
  - `uv.lock` is the committed lockfile — reproducible installs.
  - Workflow: `cd <course> && uv sync` (creates `.venv`, installs from lock).
  - Legacy `requirements.txt` files are migrated when a course is next
    touched: convert deps into `[project] dependencies`, then `uv lock`.
- `pyproject.toml` and `uv.lock` are **committed**; `.venv/` is gitignored.

## Keeping the repo slim
- Target: repo stays well under ~100 MB.
- No videos, no `.mat`/`.h5` datasets, no model weights, no large CSVs
  in git. Course media and datasets are re-downloaded on demand;
  document the source URL in the course README.
- `.DS_Store`, `__pycache__/`, `*.pyc`, `.ipynb_checkpoints/` are
  gitignored — never commit them.
- Prefer clearing notebook outputs before committing.

## House rules
- Personal repo: work on `main` directly by default; use branches
  when a change is big or experimental.
- Never delete a course folder without explicit confirmation.
