from abc import ABC, abstractmethod

class ICommand(ABC):
    '''Interface for commands'''
    
    @abstractmethod
    def execute(self, **kwargs):
        pass