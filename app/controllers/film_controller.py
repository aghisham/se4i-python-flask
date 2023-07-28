from app import app
from flask import request, jsonify, render_template
from app.models.film import Film
import json

data = json.load(open("app/static/films.json"))
films_list = data

app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = MongoClient(app.config['MONGO_URI'])
db = mongo.mydatabase


@app.route('/')
def index():
    return render_template('filmIndex.html')


@app.route("/films/<title>", methods=["GET"])
def list_films(title):
    for film in films_list:
        if film["Title"] == title:
            return jsonify(film)
    return jsonify({"message": "Not existe"}), 400


@app.route("/films/<title>/<year>/<rated>", methods=["POST"])
def add(title, year, rated):
    try:
        temp_film = Film(
            title,
            year,
            rated,
        )
        temp_film.store()
    except Exception:
        return jsonify({"message": "fail"}), 400
    return jsonify({"message": "success"}), 200


@app.route("/films", methods=["GET"])
def display():
    return jsonify(films_list), 200
