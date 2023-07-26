from flask import Blueprint, request, jsonify
from bson.json_util import dumps
from flask_apispec import doc, use_kwargs, marshal_with
from app.models.user import User, UserSchema, DefaultResponseSchema
from app import app, DB, DOCS


users_bp = Blueprint(
    "users_bp", __name__, template_folder="templates", static_folder="static"
)


@users_bp.route("", methods=["GET"], provide_automatic_options=False)
@doc(description="Get All Users", tags=["Users"])
@marshal_with(UserSchema(many=True))
def index():
    """Get users list

    Returns:
        str: users list
    """
    cursor = DB.users.find({}).limit(20)  # type: ignore
    return jsonify(dumps(cursor))


@users_bp.route("", methods=["POST"], provide_automatic_options=False)
@doc(description="Insert User", tags=["Users"])
@use_kwargs(UserSchema, location=("json"))
@marshal_with(DefaultResponseSchema())
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


@users_bp.route("/<int:id>", methods=["GET"], provide_automatic_options=False)
@doc(description="Get User", tags=["Users"])
@marshal_with(UserSchema(many=False))
def show(id):
    """Get user by id

    Args:
        id (int): user id

    Returns:
        dict: User
    """
    user = DB.users.find_one({"id": id})  # type: ignore
    if user:
        return jsonify(dumps(user))
    return jsonify({"message": "Not existe"}), 400


@users_bp.route("/<int:id>", methods=["PUT"], provide_automatic_options=False)
@doc(description="Update User", tags=["Users"])
@use_kwargs(UserSchema, location=("json"))
@marshal_with(DefaultResponseSchema())
def update(id):
    """Update user data

    Args:
        id (int): user id

    Returns:
        str: succes or fail
    """
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
        return jsonify({"message": "success"}), 200
    except Exception:
        return jsonify({"message": "Not existe"}), 400


app.register_blueprint(users_bp, url_prefix="/users")
DOCS.register(index, blueprint="users_bp")
DOCS.register(store, blueprint="users_bp")
DOCS.register(show, blueprint="users_bp")
DOCS.register(update, blueprint="users_bp")
