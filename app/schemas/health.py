from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    version: str
    name: str


class ProviderHealthResponse(BaseModel):
    provider: str
    status: str
    detail: str | None = None
