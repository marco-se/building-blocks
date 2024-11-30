from API_LIBRARY.core.manager_commands.ICommand import ICommand
from API_LIBRARY.core.services.hello_service import HelloService

class HelloCommand (ICommand):
    '''Command for getting hello world'''
    
    def __init__(self, hello_service:HelloService):
        self.__hello_service: HelloService = hello_service

    def execute(self) -> str:
        '''Execute command'''
        return self.__hello_service.get_hello_world()
