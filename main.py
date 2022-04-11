from fastapi import FastAPI
import routes
from di_container import Container


def create_app() -> FastAPI:
    container = Container()
    container.config.from_yaml('config/config.yaml')
    container.wire(modules=[
        routes
    ])
    app = FastAPI()
    app.container = container
    app.include_router(routes.router)

    return app


app = create_app()


@app.on_event('startup')
async def startup():
    await app.container.user_client().connect()
    print('connection db')


@app.on_event('shutdown')
async def shutdown():
    await app.container.user_client().disconnect()
    print('disconnecting db')
