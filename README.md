# backend-practice

Python practice for studying backend development.

This project uses [uv](https://docs.astral.sh/uv/) for Python versions, dependencies and running code.

## Setup

Install uv (macOS):

```bash
brew install uv
```

Create the project metadata (first time only, skip if `pyproject.toml` exists):

```bash
uv init --bare
```

Install dependencies and create `.venv`:

```bash
uv sync
```

## Usage

```bash
uv add <package>          # add a dependency
uv add --dev pytest       # add a dev dependency
uv remove <package>       # remove a dependency
uv run python <file>.py   # run a script in the project environment
uv run pytest             # run tests
uv run ruff check         # lint
uv run ruff check --fix   # lint and auto-fix
uv run ruff format        # format
```

Commit `pyproject.toml` and `uv.lock`; `.venv/` is ignored.
