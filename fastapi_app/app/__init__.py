"""Init App"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.testclient import TestClient
import app.config as conf
from app.routers import home_controller, user_controller


app = FastAPI(
    title=conf.APP_NAME,
    version=conf.APP_VERSION,
    description=conf.APP_DESCRIPTION,
    debug=conf.DEBUG,
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(home_controller.ROUTER)
app.include_router(user_controller.ROUTER)


CLIENT = TestClient(app)