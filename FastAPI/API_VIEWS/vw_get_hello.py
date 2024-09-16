from fastapi import APIRouter, HTTPException
from API_LIBRARY.core.dto import HelloDTO
from API_LIBRARY.core.manager_commands.command_host import CommandHost

COMMAND_HOST = CommandHost()

get_hello_router = APIRouter(
    prefix="/hello",
    tags=["hello"],
    responses={404: {"description": "Not found"}},
)

@get_hello_router.get(
    path="/",
    description="Get hello world.",
    response_model=HelloDTO)
async def get_hello():
    try:
        res: HelloDTO = {"response": COMMAND_HOST.HelloCommand()}
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
