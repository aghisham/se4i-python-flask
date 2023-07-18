from flask import Flask
# from flask_jwt import JWT
#from flask_cors import CORS
from app.models.user import User
import datetime
import json
import logging
import uuid

logging.basicConfig(
    level=logging.INFO|logging.ERROR,
    filename="log.log",
    format="%(asctime)s %(levelname)s %(message)s",
)

app = Flask(__name__)


app.config["SECRET_KEY"] = uuid.uuid4().hex
#app.config["JWT_EXPERATION_DELTA"] = datetime.timedelta(days=2)
#app.config["JWT_AUTH_URL_RULE"] = "/auth"


def authenticate(username, password):
    data = json.load(open("app/static/users_list.json"))
    users_list = data if (len(data)) else []
    for user in users_list:
        if user["email"] == username and user["password"] == password:
            return User(user["id"], user["firstName"], user["lastName"], user["email"], user["password"], user["birthDate"])
    return None


def identity(payload):
    data = json.load(open("app/static/users_list.json"))
    users_list = data if (len(data)) else []
    for user in users_list:
        if user["id"] == payload["identity"]:
            return User(user["id"], user["firstName"], user["lastName"], user["email"], user["password"], user["birthDate"])
    return None


#CORS(app, resources={r"/": {"origins": "localhost:*"}})
# JWT(app=app, authentication_handler=authenticate, identity_handler=identity)
from app.controllers import *


