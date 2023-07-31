from app import app
from flask import request, jsonify, render_template
import jwt


from app.config import user_name1, password1, user_id1
from app.config import config

print(user_id1, user_name1, password1, config["development"].SECRET_KEY)
# just to test, the user and pass should be retrieved from database and the pass should be encrypted.
users = {user_name1: {"user_id": user_id1, "password": password1}}

@app.route("/pylogin-form")
def index1_jwt():
    return render_template("login.html")


@app.route("/pyjwt-login", methods=["POST"])
def login1():
    if request.is_json:
        data = request.get_json()
        username = data.get("username")
        password1 = data.get("password")
    else:
        username = request.form.get("username")
        password1 = request.form.get("password")

    if not username or not password1:
        return jsonify({"message": "Missing username or password"}), 400

    if username not in users or users[username]["password"] != password1:
        return jsonify({"message": "Invalid username or password"}), 401

    user_id1 = users[username]["user_id"]
    payload = {"user_id": user_id1, "username": username}
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
        user_id1 = decoded_token["user_id"]
        username = decoded_token["username"]

        # Perform any additional authentication or authorization checks based on user_id or username
        if user_id1 == 147852:
            return jsonify({"message": f"Authorized user {username} with ID {user_id1}"})
        return jsonify(
            {"message": f"Protected resource for user {username} with ID {user_id1}"}
        )
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401
