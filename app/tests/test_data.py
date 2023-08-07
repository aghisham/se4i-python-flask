import json
from app import app

def test_get_dec_route():
    response = app.test_client().get("/datas")
    with open('app/static/data_list.json') as mon_fichier:
     data = json.load(mon_fichier)
    assert response.status_code == 200
    assert data
    
def test_put_r():
    response = app.test_client().put(
        "/datas/update/1",
        json={
            "id": 1,
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964,
            "dec": "original from America",
        },
    )
    assert response.status_code == 200
    
def test_post_r():
    response = app.test_client().post(
        "/datas/1",
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
    response = app.test_client().delete("datas/delete/1")
    assert response.status_code == 200

def test_post_jwt():
    response = app.test_client().post(
        "/datas/pyjwt-login",
        json={
            "id": 1,
            "username": "zakaria",
            "password": "password789",
         },
    )
    assert response.status_code == 200
