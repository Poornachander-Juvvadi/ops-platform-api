import logging
from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from app.api.v1.router import v1_router
from app.core.config import get_settings
from app.core.exceptions import AppError, app_exception_handler, http_exception_handler
from app.middleware.logging import RequestLoggingMiddleware
from app.schemas.health import HealthResponse
from app.services.health import get_health

settings = get_settings()

logging.basicConfig(
    level=getattr(logging, settings.log_level.upper(), logging.INFO),
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http_client = httpx.AsyncClient(
        timeout=httpx.Timeout(float(settings.http_client_timeout)),
        limits=httpx.Limits(
            max_connections=settings.http_client_max_connections,
            max_keepalive_connections=20,
        ),
    )
    yield
    await app.state.http_client.aclose()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)

# Middleware (order matters: last added = first executed)
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handlers
app.add_exception_handler(AppError, app_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)

# Routers
app.include_router(v1_router)


@app.get("/health", tags=["Health"])
async def health_check() -> HealthResponse:
    return get_health()
