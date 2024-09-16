from pydantic import BaseModel

class HelloDTO(BaseModel):
    response: str