from flask import Blueprint, request, jsonify
from bson.json_util import dumps
from app.models.user import User
from app import DB


users_bp = Blueprint(
    "users_bp", __name__, template_folder="templates", static_folder="static"
)


@users_bp.route("", methods=["GET"])
def index():
    """Get users list

    Returns:
        str: users list
    """
    cursor = DB.users.find({})  # type: ignore
    return jsonify(dumps(cursor))


@users_bp.route("", methods=["POST"])
def store():
    """Add user to users list

    Returns:
        str: succes or fail
    """
    try:
        if request.json:
            user_model = User(
                request.json["id"],
                request.json["first_name"],
                request.json["last_name"],
                request.json["email"],
                request.json["password"],
                request.json["birthDate"],
            )
            user_model.store()
    except Exception:
        return jsonify({"message": "fail"}), 400
    return jsonify({"message": "success"}), 200


@users_bp.route("/<int:id>", methods=["GET", "PUT"])
def show(id):
    """Get user by id and update user data

    Args:
        id (int): user id

    Returns:
        str: succes or fail
    """
    if request.method == "GET":
        user = DB.users.find_one({"id": id})  # type: ignore
        if user:
            return jsonify(dumps(user))
        return jsonify({"message": "Not existe"}), 400
    else:
        try:
            if request.json:
                user_model = User(
                    id,
                    request.json["first_name"],
                    request.json["last_name"],
                    request.json["email"],
                    request.json["password"],
                    request.json["birthDate"],
                )
                user_model.update()
        except Exception:
            return jsonify({"message": "Not existe"}), 400
        return jsonify({"message": "success"}), 200
