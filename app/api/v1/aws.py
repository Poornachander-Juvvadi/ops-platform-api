from fastapi import APIRouter

router = APIRouter(prefix="/aws", tags=["AWS"])


@router.get("/status")
async def aws_status() -> dict:
    return {"provider": "aws", "status": "available"}
