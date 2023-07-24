import logging
import json
from flask import session
from app.models.user import User


logging.basicConfig(
    level=logging.INFO | logging.ERROR,
    filename="log.log",
    format="%(asctime)s %(levelname)s %(message)s",
)


def authenticate(username, password):
    """Authenticate user

    Returns:
        User|None
    """
    data = json.load(open("app/static/users_list.json", mode="r", encoding="utf-8"))
    users_list = data if (len(data)) else []
    for user in users_list:
        if user["email"] == username and user["password"] == password:
            session["username"] = f"{user['first_name']} {user['last_name']}"
            return User(
                user["id"],
                user["first_name"],
                user["last_name"],
                user["email"],
                user["password"],
                user["birthDate"],
            )
    return None


def identity(payload):
    """Get current user

    Returns:
        User|None
    """
    data = json.load(open("app/static/users_list.json", mode="r", encoding="utf-8"))
    users_list = data if (len(data)) else []
    for user in users_list:
        if user["id"] == payload["identity"]:
            return User(
                user["id"],
                user["first_name"],
                user["last_name"],
                user["email"],
                user["password"],
                user["birthDate"],
            )
    return None
