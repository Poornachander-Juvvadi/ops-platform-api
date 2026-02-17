from fastapi import APIRouter

router = APIRouter(prefix="/splunk", tags=["Splunk"])


@router.get("/status")
async def splunk_status() -> dict:
    return {"provider": "splunk", "status": "available"}
