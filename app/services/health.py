from app.core.config import get_settings
from app.schemas.health import HealthResponse


def get_health() -> HealthResponse:
    settings = get_settings()
    return HealthResponse(
        status="healthy",
        version=settings.app_version,
        name=settings.app_name,
    )
