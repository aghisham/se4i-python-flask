import pytest
import json
from app import app
import static


def test_get_dec_route():
    response = app.test_client().get("/get-dec")
    data = json.loads(response.data)
    for x in static.data_list:
        dec = data["desc"]
        assert response.status_code == 200
        assert dec == "original from Spain"


def test_get_r():
    response = app.test_client().get("/data/1")
    assert response.status_code == 200


def test_post_r():
    response = app.test_client().post(
        "/data",
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
