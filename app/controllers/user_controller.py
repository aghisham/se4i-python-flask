from app import app
from flask import request, jsonify
from app.models.user import User
import json


data = json.load(open('app/static/users_list.json'))
users_list = data if (len(data)) else []


@app.route("/users", methods=["GET"])
def index():
    """ Get users list

    Returns:
        str: users list
    """
    return jsonify(users_list)


@app.route("/users/<int:id>", methods=["GET", "PUT"])
def show(id):
    """ Get user by id and update user data

    Args:
        id (int): user id

    Returns:
        str: succes or fail
    """
    if request.method == 'GET':
        for user in users_list:
            if user['id'] == id:
                return jsonify(user)
        return jsonify({'message': 'Not existe'}), 400
    else:
        try:
            if (request.json):
                userModel = User(id, request.json['firstName'], request.json['lastName'],
                                 request.json['email'], request.json['password'], request.json['birthDate'])
                userModel.update()
        except:
            return jsonify({'message': 'Not existe'}), 400
        return jsonify({'message': 'success'}), 200


@app.route("/users", methods=["POST"])
def store():
    """ Add user to users list

    Returns:
        str: succes or fail
    """
    try:
        if (request.json):
            userModel = User(request.json['id'], request.json['firstName'], request.json['lastName'],
                             request.json['email'], request.json['password'], request.json['birthDate'])
            userModel.store()
    except:
        return jsonify({'message': 'fail'}), 400
    return jsonify({'message': 'success'}), 200
