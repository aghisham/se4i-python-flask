from app import app
from flask import Flask, request, render_template, jsonify
import json

# data = json.load(open('app/static/films.json'))
data = json.load(open("app/static/data_list.json"))

films_list = data
app = Flask(__name__)


@app.route("/films/<title>", methods=["POST", "GET"])
def list_films(title):
    if request.method == "POST":
        pass
    else:
        for film in films_list:
            if film["Title"] == title:
                return jsonify(film)
        return jsonify({"message": "Not existe"}), 400


@app.route("/films", methods=["GET"])
def display():
    return jsonify(films_list)
