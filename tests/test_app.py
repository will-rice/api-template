"""Tests for the FastAPI application."""

from fastapi.testclient import TestClient

from api.app import create_app


def test_health() -> None:
    """Return a successful health response."""
    client = TestClient(create_app())

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
