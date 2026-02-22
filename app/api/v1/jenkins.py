from fastapi import APIRouter

router = APIRouter(prefix="/jenkins", tags=["Jenkins"])


@router.get("/status")
async def jenkins_status() -> dict:
    return {"provider": "jenkins", "status": "available"}
