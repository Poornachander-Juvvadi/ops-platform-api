from fastapi import APIRouter

router = APIRouter(prefix="/grafana", tags=["Grafana"])


@router.get("/status")
async def grafana_status() -> dict:
    return {"provider": "grafana", "status": "available"}
