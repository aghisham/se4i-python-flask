from app import CLIENT


def test_get_users():
    response = CLIENT.get("/user")
    assert response.status_code == 200


def test_get_user():
    response = CLIENT.get("/user/1")
    assert response.status_code == 200
