# Python Piscine - 42

My solutions to the 42 Python piscine (Python for Data Science).
Each module is in its own folder.

## Modules

| Module | Folder | Topic | Status | Grade |
|--------|--------|-------|--------|-------|
| Python - 0 - Starting  | [`python-0`](python-0) | Python basics | Done | 100 |
| Python - 1 - Array     | [`python-1`](python-1) | Arrays, NumPy, images | Done | - |
| Python - 2 - DataTable | [`python-2`](python-2) | pandas, matplotlib | Not started | - |
| Python - 3 - OOP       | `python-3` | Object-oriented programming | Not started | - |
| Python - 4 - Dod       | `python-4` | Data-oriented design | Not started | - |

## Setup

Use the same Python version as the 42 machines (3.10):

```bash
uv venv --python 3.10 .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## Norm

Every file must pass flake8:

```bash
flake8 --exclude .venv .
```

Ruff auto-fixes most flake8 issues, configured in `ruff.toml`:

```bash
ruff format . && ruff check --fix .
```

## Run an exercise

```bash
cd python-0/ex00
python3 <script>.py
```
