FROM ghcr.io/astral-sh/uv:0.12.18-python3.13-trixie-slim

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
COPY src ./src

RUN uv sync --locked --no-dev

CMD ["uv", "run", "--no-sync", "fastapi", "run", "src/api/app.py", "--port", "80"]
