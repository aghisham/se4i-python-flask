from flask import Flask
# from flask_jwt import JWT
from flask_cors import CORS
import datetime
import json
import logging

logging.basicConfig(
    level=logging.INFO|logging.ERROR,
    filename="log.log",
    format="%(asctime)s %(levelname)s %(message)s",
)

app = Flask(__name__)


app.config["SECRET_KEY"] = "123é&123321123321eDSDSqdfsqf@sdfQSBF__"
app.config["JWT_EXPERATION_DELTA"] = datetime.timedelta(days=2)
app.config["JWT_AUTH_URL_RULE"] = "/auth"


def authenticate(username, password):
    data = json.load(open("app/static/users_list.json"))
    users_list = data if (len(data)) else []
    for user in users_list:
        if user["email"] == username and user["password"] == password:
            logging.info(user)
            return user
    return None


def identity(payload):
    data = json.load(open("app/static/users_list.json"))
    users_list = data if (len(data)) else []
    for user in users_list:
        if user["id"] == payload["identity"]:
            return user
    return None


CORS(app, resources={r"/": {"origins": "localhost:*"}})
# JWT(app=app, authentication_handler=authenticate, identity_handler=identity)


from app.controllers import *
