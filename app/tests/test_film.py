import json
from flask import jsonify
from app import app

data = json.load(open("app/static/films.json"))
films_list = data if (len(data)) else []


def test_display_all_route():
    response = app.test_client().get("/films")
    assert response.status_code == 200
    assert len(json.loads(response.data.decode("utf-8")))


def test_get_title_route():
    response = app.test_client().get("/films/Avatar")
    assert response.status_code == 200
