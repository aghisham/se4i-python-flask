import logging
import uuid
import datetime
import os


logging.basicConfig(
    level=logging.INFO | logging.ERROR,
    filename="log.log",
    format="%(asctime)s %(levelname)s %(message)s",
)


class Configurations:
    """Configurations Class"""

    # ---------- JWT
    SECRET_KEY = uuid.uuid4().hex
    JWT_SECRET_KEY = uuid.uuid4().hex
    JWT_EXPERATION_DELTA = datetime.timedelta(days=2)


class DevelopmentConfig(Configurations):
    """Development Configuration Class"""

    DEBUG = os.environ.get("DEBUG") or True
    MONGO_URI = os.environ.get("MONGO_URI") or "mongodb://localhost:27017/se4idata"


class TestingConfig(Configurations):
    """Testing Configuration Class"""

    DEBUG = os.environ.get("DEBUG") or False
    TESTING = os.environ.get("TESTING") or True
    MONGO_URI = os.environ.get("MONGO_URI") or "mongodb://localhost:27017/se4idata"


class ProductionConfig(Configurations):
    """Production Configuration Class"""

    DEBUG = os.environ.get("DEBUG") or False
    MONGO_URI = os.environ.get("MONGO_URI") or ""


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}

#read data from config.yaml one time and share it between the files
import json

with open('app/config.yaml', 'r') as file:
    config_data = json.load(file)

mongodb_host = config_data["mongodb"]["host"]
port = config_data["mongodb"]["port"]
database_name = config_data["mongodb"]["database_name"]
collection_name = config_data["mongodb"]["collection_name"]
user_name = config_data["jwt_credentials"]["user_name"]
password = config_data["jwt_credentials"]["password"]
user_id = config_data["jwt_credentials"]["user_id"]
api = config_data["api"]["host"]