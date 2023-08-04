from flask import jsonify, render_template, request, Blueprint
import jwt
from app import DOCS, app
from app.config import user_name, password, user_id
from app.config import config
from marshmallow import Schema, fields
from flask_apispec import doc, use_kwargs, marshal_with

print(user_id, user_name, password, config["development"].SECRET_KEY)
# just to test, the user and pass should be retrieved from the database and the pass should be encrypted.
users = {user_name: {"user_id": user_id, "password": password}}


class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)


class TokenResponseSchema(Schema):
    access_token = fields.String()


class ProtectedResponseSchema(Schema):
    message = fields.String()


jwt_authentication_bp = Blueprint("jwt_authentication_bp", __name__)


@app.route("/login-form")
def index_jwt():
    return render_template("jwt_login.html")


@app.route("/jwt-login", methods=["POST"], provide_automatic_options=False)
@doc(description="Login and get JWT token", tags=["Authentication"])
@use_kwargs(LoginSchema, location="json")
@marshal_with(TokenResponseSchema())
def login(**kwargs):
    username = kwargs["username"]
    password = kwargs["password"]

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    if username not in users or users[username]["password"] != password:
        return jsonify({"message": "Invalid username or password"}), 401

    user_id = users[username]["user_id"]
    payload = {"user_id": user_id, "username": username}
    token = jwt.encode(payload, config["development"].SECRET_KEY, algorithm="HS256")

    return {"access_token": token}


@app.route("/jwt-protected", methods=["GET"], provide_automatic_options=False)
@doc(description="Protected resource using JWT token", tags=["Protected"])
@marshal_with(ProtectedResponseSchema())
def protected():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message": "Missing token"}), 401

    try:
        key = config["development"].SECRET_KEY
        decoded_token = jwt.decode(token, key, algorithms=["HS256"])
        user_id = decoded_token["user_id"]
        username = decoded_token["username"]

        # Perform any additional authentication or authorization checks based on user_id or username
        if user_id == 1234:
            return {"message": f"Authorized user {username} with ID {user_id}"}
        return {"message": f"Protected resource for user {username} with ID {user_id}"}
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401


# Add the Blueprint to the app and register the API endpoints with Flask-apispec
app.register_blueprint(jwt_authentication_bp, url_prefix="/api")
DOCS.register(login)
DOCS.register(protected)
