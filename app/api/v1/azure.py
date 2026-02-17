from fastapi import APIRouter

router = APIRouter(prefix="/azure", tags=["Azure"])


@router.get("/status")
async def azure_status() -> dict:
    return {"provider": "azure", "status": "available"}
