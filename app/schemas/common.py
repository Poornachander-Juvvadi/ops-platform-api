from pydantic import BaseModel


class ErrorDetail(BaseModel):
    detail: str
    status_code: int


class ErrorResponse(BaseModel):
    error: ErrorDetail


class PaginationParams(BaseModel):
    page: int = 1
    page_size: int = 20


class PaginatedResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: list
