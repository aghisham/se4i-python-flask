import pytest
from flask import Flask ## import Flask


@pytest.fixture()
def app():
    print("start creating app ....")

    app = Flask(__name__)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()
   