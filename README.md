# api-template

A FastAPI service template managed with uv.

## Local development

```bash
uv run fastapi dev src/api/app.py
```

The health endpoint is available at `http://127.0.0.1:8000/health`.

## Tests and checks

```bash
uv run pytest
uv run pre-commit run -a
```

## Docker

```bash
docker build -t api-template .
docker run --rm -p 8000:80 api-template
```

Or run with Compose:

```bash
docker compose up --build
```
