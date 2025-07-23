from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from services.api_handler import yacht_handler

router = APIRouter(prefix="/api")


@router.get("/all", response_class=PlainTextResponse)
async def get_yachts():
    response = yacht_handler.get_content()
    if response["status"] == "error":
        return {"status": "error", "code": response["code"], "message": "An error occurred while fetching data."}, response["code"]
    return response["content"]