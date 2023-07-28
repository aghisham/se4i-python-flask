from app import app
from flask import request, jsonify, render_template
import jwt

from app.config import user_name, password, user_id
from app.config import config

print(user_id, user_name, password, config["development"].SECRET_KEY)
# just to test, the user and pass should be retrieved from database and the pass should be encrypted.
users = {user_name: {"user_id": user_id, "password": password}}


@app.route("/login-form")
def index_jwt():
    return render_template("jwt_login.html")


@app.route("/jwt-login", methods=["POST"])
def login():
    if request.is_json:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
    else:
        username = request.form.get("username")
        password = request.form.get("password")

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    if username not in users or users[username]["password"] != password:
        return jsonify({"message": "Invalid username or password"}), 401

    user_id = users[username]["user_id"]
    payload = {"user_id": user_id, "username": username}
    token = jwt.encode(payload, config["development"].SECRET_KEY, algorithm="HS256")

    return jsonify({"access_token": str(token)})


@app.route("/jwt-protected", methods=["GET"])
def protected():
    token = request.args["Authorization"]
    if not token:
        return jsonify({"message": "Missing token"}), 401

    try:
        key = config["development"].SECRET_KEY
        decoded_token = jwt.decode(token, key, True, "HS256")
        user_id = decoded_token["user_id"]
        username = decoded_token["username"]

        # Perform any additional authentication or authorization checks based on user_id or username
        if user_id == 1234:
            return jsonify({"message": f"Authorized user {username} with ID {user_id}"})
        return jsonify(
            {"message": f"Protected resource for user {username} with ID {user_id}"}
        )
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401
