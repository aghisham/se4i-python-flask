import os
from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

from flask_socketio import SocketIO
from flask_apispec.extension import FlaskApiSpec
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from dotenv import load_dotenv
import app.config as conf

# from flask_jwt_extended import JWTManager


load_dotenv(".env")
MODE = os.environ.get("MODE") or "development"  # development - testing - production


# ------ Init App
app = Flask(__name__)
app.config.from_object(conf.config[MODE])


# ------ Init JWT and CORS
CORS(app, resources={r"/": {"origins": "localhost:*"}})
# JWTManager(app)


# ------ Init DB
DB = PyMongo(app).db


# ------ Init Socket
socketio = SocketIO(app)


# ------ Init Swagger
app.config.update(
    {
        "APISPEC_SPEC": APISpec(
            title="Swagger S4I",
            version="v1",
            plugins=[MarshmallowPlugin()],
            openapi_version="2.0.0",
        ),
        "APISPEC_SWAGGER_URL": "/swagger/",  # URI to access API Doc JSON
        "APISPEC_SWAGGER_UI_URL": "/swagger-ui/",  # URI to access UI of API Doc
    }
)
DOCS = FlaskApiSpec(app)


# ------ Import controllers
from app.controllers import *
