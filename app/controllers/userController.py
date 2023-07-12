from app import app
from flask import request, jsonify
from app.models.user import User


@app.route("/users", methods=["GET"])
def index():
    userModel = User()
    return jsonify(userModel.users)


@app.route("/users/<int:id>", methods=["GET", "PUT"])
def show(id):
    userModel = User()
    if request.method == 'GET':
        for user in userModel.users:
            if user['id'] == id:
                return jsonify(user)
        return jsonify({'message': 'Not existe'}), 400
    else:
        try:
            if (request.json):
                userModel.update(id, request.json['firstName'], request.json['lastName'],
                                request.json['email'], request.json['password'], request.json['birthDate'])
        except:
            return jsonify({'message': 'Not existe'}), 400
        return jsonify({'message': 'success'}), 200


@app.route("/users", methods=["POST"])
def store():
    try:
        if (request.json):
            userModel = User()
            userModel.store(request.json['id'], request.json['firstName'], request.json['lastName'],
                            request.json['email'], request.json['password'], request.json['birthDate'])
    except:
        return jsonify({'message': 'fail'}), 400
    return jsonify({'message': 'success'}), 200
