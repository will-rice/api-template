"""FastAPI application."""

from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create the FastAPI application."""
    application = FastAPI(title="API")

    @application.get("/health")
    def health() -> dict[str, str]:
        """Report service health."""
        return {"status": "ok"}

    return application


app = create_app()
