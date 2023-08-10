"""Init App"""
from fastapi import FastAPI
import app.config as conf


app = FastAPI(
    title=conf.APP_NAME,
    version=conf.APP_VERSION,
    description=conf.APP_DESCRIPTION,
    debug=conf.DEBUG,
)


from app.controllers import *
