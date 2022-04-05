from fastapi import FastAPI
from routes import router
from UserPostgresService import user_service


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)

    return app


app = create_app()


@app.on_event('startup')
async def startup():
    await user_service.connect()
    print('connection db')


@app.on_event('shutdown')
async def shutdown():
    await user_service.disconnect()
    print('disconnecting db')
