from app import app
from flask import jsonify, request
from app.models.item import ItemStore
import requests
from app.config import api


API_BASE_URL = api


@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    response = requests.post(API_BASE_URL, json=data)
    if response.status_code == 201:
        item = response.json()
        return jsonify(item), 201
    else:
        return jsonify({"error": "Failed to create item"}), response.status_code


@app.route("/items/<int:id>", methods=["GET"])
def get_item(id):
    response = requests.get(f"{API_BASE_URL}/{id}")
    if response.status_code == 200:
        item = response.json()
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), response.status_code


@app.route("/items/<int:id>", methods=["PUT"])
def update_item(id):
    data = request.get_json()
    response = requests.put(f"{API_BASE_URL}/{id}", json=data)
    if response.status_code == 200:
        item = response.json()
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), response.status_code


@app.route("/items/<int:id>", methods=["DELETE"])
def delete_item(id):
    response = requests.delete(f"{API_BASE_URL}/{id}")
    if response.status_code == 200:
        return jsonify({"message": "Item deleted"})
    else:
        return jsonify({"error": "Item not found"}), response.status_code
