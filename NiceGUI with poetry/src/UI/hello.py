from nicegui import APIRouter, ui
from API_LIBRARY.core.manager_commands.command_host import CommandHost

COMMAND_HOST = CommandHost()

router = APIRouter()

@router.page("/")
async def get_hello():
    ui.page_title('Hello World')
    ui.dark_mode(True)
    ui.label(COMMAND_HOST.HelloCommand())
