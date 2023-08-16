"""Init App"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.testclient import TestClient
from app.models import *
from app.db import Base, engine
from app.routers import user, home
import app.config as conf


app = FastAPI(
    title=conf.APP_NAME,
    version=conf.APP_VERSION,
    description=conf.APP_DESCRIPTION,
    debug=conf.DEBUG,
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
Base.metadata.create_all(bind=engine)

# Add routes
app.include_router(home.ROUTER, prefix="", tags=["Home"])
app.include_router(user.ROUTER, prefix="/user", tags=["Users"])


CLIENT = TestClient(app)
