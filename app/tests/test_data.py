import pytest
import json
from app import app

def test_get_dec_route():
    response = app.test_client().get("/get-dec")
    assert response.status_code == 200
    assert len(json.loads(response.data.decode("utf-8")))


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
