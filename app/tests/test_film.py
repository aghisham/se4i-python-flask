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


def test_save_in_db():
    response = app.test_client().get("/films/save")
    assert response.status_code == 200
    assert response.data == b"data imported"


def test_get_films():
    response = app.test_client().get("/films")
    assert response.status_code == 200


def test_get_film_name():
    response = app.test_client().get("/films/Avatar")
    assert response.status_code == 200
    res = response.data.decode("utf-8")
    res_dict = json.loads(res)
    assert res_dict["success"] is True


def test_create_film():
    response = app.test_client().post(
        "/films", json={"Title": "Film TEST", "Rated": "Rated Test", "Year": 2000}
    )
    assert response.status_code == 200
    res = response.data.decode("utf-8")
    res_dict = json.loads(res)
    assert res_dict["success"] is True


def test_update_film():
    response = app.test_client().put(
        "/films/Film TEST", json={"Title": "Film TEST UPDATED", "Rated": "Rated Test", "Year": 2000}
    )
    assert response.status_code == 200
    res = response.data.decode("utf-8")
    res_dict = json.loads(res)
    assert res_dict["success"] is True


def test_delete_film():
    response = app.test_client().delete("/films/300")
    assert response.status_code == 204


def test_set_login_cred():
    response = app.test_client().post("/log", json={
        "username": "Mohamed Ali",
        "password": "passcode"
    })

    assert response.status_code == 200
    assert "access_token" in response.get_json()
