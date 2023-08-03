from flask import Flask, jsonify, request, make_response, render_template
from app import app
from app.config import config, user_name2, password2, user_id2
import jwt

user_coll = {user_name2: {"password": password2, "user_id": user_id2}}


@app.route("/log_form")
def jwt_log_form():
    return render_template("jwt_login.html")


@app.route("/log", methods=["POST"])
def jwt_login():
    username = request.json["username"]
    password = request.json["password"]
    if not username or not password:
        return jsonify({"message": "please check username or password is empty"}), 400
    if username not in user_coll or password2 != user_coll[username]["password"]:
        return jsonify({"message": "username or password provided is not correct"}), 401

    user_id = user_coll[username]["user_id"]
    payload = {"user_id": user_id, "username": username}
    token = jwt.encode(payload, config["development"].SECRET_KEY, algorithm="HS256")

    return jsonify({"access_token": str(token)})


@app.route("/unprotected_route", methods=["GET"])
def protected_route():
    token = request.args["Authorization"]
    if not token:
        return jsonify({"message": "Missing token"}), 401
    try:
        key = config["development"].SECRET_KEY
        decoded_token = jwt.decode(token, key, True, "HS256")
        user_id = decoded_token["user_id"]
        username = decoded_token["username"]
        return "welcome this is protected route and you are eligible to see it"
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401


@app.route("/unprotected_route", methods=["GET"])
def unprotected_route():
    return "This is an unprotected route"
