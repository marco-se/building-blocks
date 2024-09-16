from dependency_injector import containers, providers
from API_LIBRARY.core.manager_commands.command_init import CommandInit
from API_LIBRARY.core.services import HelloService
from API_LIBRARY.core.manager_commands.commands import HelloCommand

class ServicesContainer(containers.DeclarativeContainer):
    '''Container that holds all necessary services'''
    hello_service = providers.Singleton(HelloService)

class CommandContainer(containers.DeclarativeContainer):
    '''Container that holds all necessary commands'''
    command_init = providers.Singleton(
        CommandInit,
        providers.Singleton(
            HelloCommand,
            hello_service=ServicesContainer.hello_service
        )
    )

    wiring_config = containers.WiringConfiguration(modules=[".manager_commands.command_host"])