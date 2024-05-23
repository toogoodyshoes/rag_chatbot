from fastapi import APIRouter

router = APIRouter(
    prefix="/indexing",
    tags=["indexing"]
)


@router.get("/load")
async def load():
    return