from API_LIBRARY.core.container import CommandContainer
from API_LIBRARY.core.manager_commands.command_init import CommandInit
from dependency_injector.wiring import inject, Provide
from API_LIBRARY.core.manager_commands.commands import HelloCommand

class CommandHost():
    '''Command host holding commands'''

    @inject
    def __init__(self, command_init: CommandInit = Provide[CommandContainer.command_init]):
        self.command_dic = command_init.command_dic

    def HelloCommand(self) -> str:
        return self.command_dic[HelloCommand].execute()
