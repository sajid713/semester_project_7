from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def get_health() -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "Backend working fine!"}
    )
