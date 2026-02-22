from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse


class AppError(Exception):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail


class ProviderError(AppError):
    """Raised when an external provider API call fails."""

    def __init__(self, provider: str, detail: str, status_code: int = 502):
        self.provider = provider
        super().__init__(status_code=status_code, detail=f"{provider}: {detail}")


class AuthenticationError(AppError):
    def __init__(self, detail: str = "Invalid or missing authentication credentials"):
        super().__init__(status_code=401, detail=detail)


class AuthorizationError(AppError):
    def __init__(self, detail: str = "Insufficient permissions"):
        super().__init__(status_code=403, detail=detail)


class NotFoundError(AppError):
    def __init__(self, resource: str, identifier: str):
        super().__init__(status_code=404, detail=f"{resource} '{identifier}' not found")


async def app_exception_handler(_request: Request, exc: AppError) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {"detail": exc.detail, "status_code": exc.status_code}},
    )


async def http_exception_handler(_request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {"detail": exc.detail, "status_code": exc.status_code}},
    )
