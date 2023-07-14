from app import app
import json


def test_index_route():
    response = app.test_client().get("/users")

    assert response.status_code == 200
    assert len(json.loads(response.data.decode("utf-8")))


def test_show_route():
    response = app.test_client().get("/users/1")

    assert response.status_code == 200


def test_update_route():
    response = app.test_client().put(
        "/users/1",
        data={
            "firstName": "test1",
            "lastName": "test1",
            "email": "test1@nttdata.com",
            "password": "654321",
            "birthDate": "01/01/1999",
        },
    )

    assert response.status_code == 200
