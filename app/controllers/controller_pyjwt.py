from app import app
from flask import request, jsonify, render_template
import jwt

# just to test, the user and pass should be retrieved from database and the pass should be encrypted.
users = {"zakaria": {"user_id": 123458, "password": "password147"}}


@app.route("/pylogin-form")
def index1_jwt():
    return render_template("jwt_login.html")


@app.route("/pyjwt-login", methods=["POST"])
def login1():
    if request.json:
        username = request.json["username"]
        password = request.json["password"]
    else:
        username = request.form.get("username")
        password = request.form.get("password")

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    if username not in users or users[username]["password"] != password:
        return jsonify({"message": "Invalid username or password"}), 401

    user_id = users[username]["user_id"]
    payload = {"user_id": user_id, "username": username}
    token = jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")

    return jsonify({"access_token": str(token)})


@app.route("/pyjwt-protected", methods=["GET"])
def protected1():
    token = request.args["Authorization"]
    if not token:
        return jsonify({"message": "Missing token"}), 401

    try:
        key = app.config["SECRET_KEY"]
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
