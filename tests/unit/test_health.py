import httpx
import pytest


@pytest.mark.asyncio
async def test_health_check(client: httpx.AsyncClient):
    response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data
    assert "name" in data


@pytest.mark.asyncio
async def test_provider_status_endpoints(client: httpx.AsyncClient):
    providers = ["aws", "azure", "grafana", "splunk", "github", "jenkins", "gitlab"]
    for provider in providers:
        response = await client.get(f"/api/v1/{provider}/status")
        assert response.status_code == 200
        data = response.json()
        assert data["provider"] == provider
        assert data["status"] == "available"
