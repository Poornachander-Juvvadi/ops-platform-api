from fastapi import APIRouter

router = APIRouter(prefix="/github", tags=["GitHub"])


@router.get("/status")
async def github_status() -> dict:
    return {"provider": "github", "status": "available"}
