import json
from app import app


def test_get_dec_route():
    response = app.test_client().get("/datas")
    with open("app/static/data_list.json") as mon_fichier:
        data = json.load(mon_fichier)
    assert response.status_code == 200
    assert data


def test_get_r():
    response = app.test_client().get("/update/1")
    assert response.status_code == 200


def test_post_r():
    response = app.test_client().post(
        "/update/1",
        json={
            "id": 1,
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964,
            "dec": "original from America",
        },
    )

    assert response.status_code == 200


def test_put_r():
    response = app.test_client().post(
        "/data/1",
        json={
            "id": 1,
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964,
            "dec": "original from America",
        },
    )
    assert response.status_code == 200


def test_delete_r():
    response = app.test_client().delete("/data/1")
    assert response.status_code == 200
