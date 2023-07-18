from app import app
from flask import request, jsonify, render_template, Flask
from app.models.project import Project
import jwt
import uuid

app.config["SECRET_KEY"] = uuid.uuid4().hex

#just to test, the user and pass should be retrieved from database and the pass should be encrypted.
users = {"hisham": {"user_id": 124587, "password": "password123"}}


@app.route("/login-form")
def index_jwt():
    return render_template("jwt_login.html")


@app.route("/jwt-login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    if username not in users or users[username]["password"] != password:
        return jsonify({"message": "Invalid username or password"}), 401

    user_id = users[username]["user_id"]
    payload = {"user_id": user_id, "username": username}
    token = jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")

    return jsonify({"token": token})


@app.route("/jwt-protected", methods=["GET"])
def protected():
    token = request.args["Authorization"]
    print(token)
    if not token:
        return jsonify({"message": "Missing token"}), 401

    try:
        key = app.config["SECRET_KEY"]
        decoded_token = jwt.decode(token, key, "HS256")
        user_id = decoded_token["user_id"]
        username = decoded_token["username"]

        # Perform any additional authentication or authorization checks based on user_id or username
        if user_id == 1234 :
            return jsonify(
            {"message": f"Authorized user {username} with ID {user_id}"}
        )
        return jsonify(
            {"message": f"Protected resource for user {username} with ID {user_id}"}
        )
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401