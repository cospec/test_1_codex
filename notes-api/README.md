
# Notes API (Flask + SQLAlchemy)

A minimal, production-ready starter for a Notes API. Good for handing off to a software-engineering agent (like **Codex**) to iterate on.

## Features
- Flask app factory pattern
- SQLAlchemy + SQLite
- CRUD for `/notes`
- Simple query search (`?q=`) and pagination (`?page=&per_page=`)
- Input validation with lightweight checks
- Pytest with an in-memory SQLite fixture
- Black + Ruff config
- Dockerfile + docker-compose
- `.env.example`

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run
FLASK_APP=app:create_app flask run
# or:
python -m app
```

## Environment
Copy `.env.example` to `.env` and customize.

## API Endpoints
- POST `/notes`  -> create
- GET `/notes`   -> list (supports `?q=`, `?page=`, `?per_page=`)
- GET `/notes/<id>` -> fetch single
- PUT `/notes/<id>` -> update (title/content)
- DELETE `/notes/<id>` -> remove

## Run tests
```bash
pytest -q
```

## Codex: Suggested first task
> Implement Phase 1 end-to-end: run tests, ensure they pass, and open a PR titled "feat: phase-1 CRUD". If tests fail, fix the code or tests minimally. Then propose a plan for Phase 2 (auth, rate limiting, CI).

## Repo layout
```
app/
  __init__.py
  main.py
  models.py
  routes.py
  config.py
tests/
  conftest.py
  test_notes_api.py
Dockerfile
docker-compose.yml
requirements.txt
pyproject.toml
.env.example
```
