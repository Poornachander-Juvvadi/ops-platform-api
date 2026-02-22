from abc import ABC, abstractmethod
from typing import Any

import httpx

from app.core.exceptions import ProviderError


class BaseProvider(ABC):
    """Base class for all external service providers."""

    def __init__(self, client: httpx.AsyncClient, base_url: str):
        self.client = client
        self.base_url = base_url.rstrip("/")

    @property
    @abstractmethod
    def provider_name(self) -> str: ...

    def _build_url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def _default_headers(self) -> dict[str, str]:
        return {"Accept": "application/json"}

    async def _request(
        self,
        method: str,
        path: str,
        headers: dict[str, str] | None = None,
        **kwargs: Any,
    ) -> httpx.Response:
        url = self._build_url(path)
        merged_headers = {**self._default_headers(), **(headers or {})}
        try:
            response = await self.client.request(method, url, headers=merged_headers, **kwargs)
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError as exc:
            raise ProviderError(
                provider=self.provider_name,
                detail=f"HTTP {exc.response.status_code}: {exc.response.text}",
                status_code=exc.response.status_code,
            ) from exc
        except httpx.RequestError as exc:
            raise ProviderError(
                provider=self.provider_name,
                detail=f"Connection error: {exc}",
            ) from exc

    async def _get(self, path: str, **kwargs: Any) -> httpx.Response:
        return await self._request("GET", path, **kwargs)

    async def _post(self, path: str, **kwargs: Any) -> httpx.Response:
        return await self._request("POST", path, **kwargs)

    async def _put(self, path: str, **kwargs: Any) -> httpx.Response:
        return await self._request("PUT", path, **kwargs)

    async def _patch(self, path: str, **kwargs: Any) -> httpx.Response:
        return await self._request("PATCH", path, **kwargs)

    async def _delete(self, path: str, **kwargs: Any) -> httpx.Response:
        return await self._request("DELETE", path, **kwargs)

    async def health_check(self) -> dict[str, str]:
        """Override in subclasses to implement provider-specific health checks."""
        return {"provider": self.provider_name, "status": "not_configured"}
