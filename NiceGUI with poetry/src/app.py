from nicegui import ui, app
from API_LIBRARY.core.container import CommandContainer, ServicesContainer

# Initialize dependency injection containers
services_container = ServicesContainer()
commands_container = CommandContainer()
commands_container.wire(modules=[__name__])
commands_container.init_resources()
services_container.init_resources()

# These imports must be below the initialization of dependency injection containers
from UI.hello import router as hello_router
app.include_router(hello_router)

# Run the application
ui.run(host="0.0.0.0", port=8000)