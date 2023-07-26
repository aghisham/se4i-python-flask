from flask import session
from flask_jwt import JWT
from app.models.user import User
from app import DB, app


def authenticate(username, password):
    """Authenticate user

    Returns:
        User|None
    """
    user = DB.users.find_one({"email": username, "password": password})  # type: ignore
    if user:
        session["username"] = f"{user['first_name']} {user['last_name']}"
        return User(
            user["id"],
            user["first_name"],
            user["last_name"],
            user["email"],
            user["password"],
            user["birth_date"],
        )
    session["username"] = None
    return None


def identity(payload):
    """Get current user

    Returns:
        User|None
    """
    user = DB.users.find_one({"id": payload["identity"]})  # type: ignore
    if user:
        return User(
            user["id"],
            user["first_name"],
            user["last_name"],
            user["email"],
            user["password"],
            user["birth_date"],
        )
    return None


JWT(app=app, authentication_handler=authenticate, identity_handler=identity)
