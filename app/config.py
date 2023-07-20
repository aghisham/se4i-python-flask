import logging
import json
from app.models.user import User


logging.basicConfig(
    level=logging.INFO | logging.ERROR,
    filename="log.log",
    format="%(asctime)s %(levelname)s %(message)s",
)


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
