import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from API_LIBRARY.core.container import CommandContainer, ServicesContainer

services_container = ServicesContainer()
commands_container = CommandContainer()
commands_container.wire(modules=[__name__])
commands_container.init_resources()
services_container.init_resources()

app = FastAPI()

origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from API_VIEWS.vw_get_hello import get_hello_router
app.include_router(get_hello_router)

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)