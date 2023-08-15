"""Init App"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.testclient import TestClient
import app.config as conf
from app.routers import home_controller, user_controller
from app.models import *
from app.db import Base, engine


app = FastAPI(
    title=conf.APP_NAME,
    version=conf.APP_VERSION,
    description=conf.APP_DESCRIPTION,
    debug=conf.DEBUG,
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
Base.metadata.create_all(bind=engine)

# Add routes
app.include_router(home_controller.ROUTER)
app.include_router(user_controller.ROUTER)


CLIENT = TestClient(app)
