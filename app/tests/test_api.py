import pytest
import json
from app import app
import requests


def test_index_route():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "hello from homepage"


def test_get_name_route():
    response = app.test_client().get("/get-name")
    data = json.loads(response.data)
    name = data["name"]
    assert response.status_code == 200
    assert name == "SE4I project"


def test_get():
    response = app.test_client().get("/items/1")
    assert response.status_code == 200


def test_post():
    response = app.test_client().post(
        "/items", json={"title": "Test Title", "body": "Test Body", "userId": 1}
    )
    assert response.status_code == 201


def test_put():
    response = app.test_client().put(
        "/items/1", json={"title": "Updated Title", "body": "Updated Body", "userId": 1}
    )
    assert response.status_code == 200


def test_delete():
    response = app.test_client().delete("/items/1")
    assert response.status_code == 200
