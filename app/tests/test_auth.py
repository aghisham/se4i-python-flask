from app import app
import json


def test_auth_route():
    # uncomment if python version <= 3.9
    # response = app.test_client().post("/auth", json={
    #     "username": "test1@nttdata.com",
    #     "password": "123456"
    # })
    # assert response.status_code == 200
    # assert "access_token" in json.loads(response.data.decode("utf-8"))
    
    response = app.test_client().post("/jwt-login", json={
        "username": "hisham",
        "password": "password123"
    })

    assert response.status_code == 200
    assert "access_token" in json.loads(response.data.decode("utf-8"))


