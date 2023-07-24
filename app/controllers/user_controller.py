import json
from flask import Blueprint, request, jsonify
from app.models.user import User


users_bp = Blueprint(
    "users_bp", __name__, template_folder="templates", static_folder="static"
)


data = json.load(open("app/static/users_list.json", mode="r", encoding="utf-8"))
users_list = data if (len(data)) else []


@users_bp.route("", methods=["GET"])
def index():
    """Get users list

    Returns:
        str: users list
    """
    return jsonify(users_list)


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
        for user in users_list:
            if user["id"] == id:
                return jsonify(user)
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
