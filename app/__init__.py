from flask import Flask
# from flask_jwt import JWT
# from flask_cors import CORS
from app.models.user import User
import datetime
import json
import logging
import uuid
from app.controllers.controller import controller_blueprint
from flask import jsonify

from app.controllers import *
from flask_cors import CORS
import uuid
import app.config as conf
import requests

# from flask_jwt import JWT # ------ uncomment if python version <= 3.9
from app.controllers.files_controller import files_bp
from app.controllers.user_controller import users_bp


logging.basicConfig(
    level=logging.INFO | logging.ERROR,
    filename="log.log",
    format="%(asctime)s %(levelname)s %(message)s",
)
app = Flask(__name__)
app.register_blueprint(controller_blueprint,  url_prefix='/controller')

app.config["SECRET_KEY"] = uuid.uuid4().hex
app.config["JWT_EXPERATION_DELTA"] = datetime.timedelta(days=2)
app.config["JWT_AUTH_URL_RULE"] = "/auth"


CORS(app, resources={r"/": {"origins": "localhost:*"}})
# JWT(app=app, authentication_handler=conf.authenticate, identity_handler=conf.identity) # ------ uncomment if python version <= 3.9


# Register Blueprints
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(files_bp, url_prefix="/upload")




def authenticate(username, password):
    data = json.load(open("app/static/users_list.json"))
    users_list = data if (len(data)) else []
    for user in users_list:
        if user["email"] == username and user["password"] == password:
            return User(
                user["id"],
                user["firstName"],
                user["lastName"],
                user["email"],
                user["password"],
                user["birthDate"],
            )
    return None


def identity(payload):
    data = json.load(open("app/static/users_list.json"))
    users_list = data if (len(data)) else []
    for user in users_list:
        if user["id"] == payload["identity"]:
            return User(
                user["id"],
                user["firstName"],
                user["lastName"],
                user["email"],
                user["password"],
                user["birthDate"],
            )
    return None


# CORS(app, resources={r"/": {"origins": "localhost:*"}})
# JWT(app=app, authentication_handler=authenticate, identity_handler=identity)



