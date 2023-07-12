import pytest
import json
from app import app

def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'hello from homepage'

def test_get_name_route():
    response = app.test_client().get('/get-name')
    data = json.loads(response.data)
    name = data['name']
    assert response.status_code == 200
    assert name == 'SE4I project'
