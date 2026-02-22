from fastapi import APIRouter

router = APIRouter(prefix="/gitlab", tags=["GitLab"])


@router.get("/status")
async def gitlab_status() -> dict:
    return {"provider": "gitlab", "status": "available"}
