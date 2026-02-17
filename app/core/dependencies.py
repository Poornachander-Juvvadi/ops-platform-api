from collections.abc import AsyncGenerator

import httpx
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import async_session_factory


async def get_http_client(request: Request) -> httpx.AsyncClient:
    return request.app.state.http_client


async def get_db(request: Request | None = None) -> AsyncGenerator[AsyncSession]:  # noqa: ARG001
    async with async_session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
