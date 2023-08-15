from app.test import CLIENT_AGENT


def test_get_users():
    """test get all users"""
    response = CLIENT_AGENT.get("/user")
    assert response.status_code == 200


def test_create_user():
    """test create user"""
    response = CLIENT_AGENT.post(
        "/user",
        json={
            "id": "2",
            "name": "test2",
            "email": "test@test.com",
            "password": "123456",
            "is_active": 1,
        },
    )
    assert response.status_code == 200


def test_get_user():
    """test get user"""
    response = CLIENT_AGENT.get("/user/2")
    assert response.status_code == 200
