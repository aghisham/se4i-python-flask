from flask import Flask, jsonify, request, make_response
from app import app


@app.route("/login")
def aaaa():
    username = request.json["username"]
    password = request.json["password"]
    if not username or not password:
        return jsonify({"message": "please check username or password is empty"}), 400
