import os
from dataclasses import dataclass

@dataclass
class EnvConfig:
    '''Dataclass that holds environment variables'''
    # CONNECTION_STRING: str

EnvConfig = EnvConfig(
    # CONNECTION_STRING = os.getenv('CONNECTION_STRING')
)