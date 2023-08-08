import logging
import uuid
import datetime
import os
import json
from dotenv import load_dotenv


load_dotenv(dotenv_path=f"{os.getcwd()}/.env")

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
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("SQLALCHEMY_DATABASE_URI")
        or "mysql://root:root@localhost/se4idata"
    )


class TestingConfig(Configurations):
    """Testing Configuration Class"""

    DEBUG = os.environ.get("DEBUG") or False
    TESTING = os.environ.get("TESTING") or True
    MONGO_URI = os.environ.get("MONGO_URI") or "mongodb://localhost:27017/se4idata"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("SQLALCHEMY_DATABASE_URI")
        or "mysql://root:root@localhost/se4idata"
    )


class ProductionConfig(Configurations):
    """Production Configuration Class"""

    DEBUG = os.environ.get("DEBUG") or False
    MONGO_URI = os.environ.get("MONGO_URI") or ""
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or ""


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}


# read data from config.yaml one time and share it between the files
try:
    with open("app/config.yaml", "r") as file:
        config_data = json.load(file)

    mongodb_host = config_data["mongodb"]["host"]
    port = config_data["mongodb"]["port"]
    database_name = config_data["mongodb"]["database_name"]
    collection_name = config_data["mongodb"]["collection_name"][0]
    user_name = config_data["jwt_credentials"]["user_name"][0]
    password = config_data["jwt_credentials"]["password"][0]
    user_id = config_data["jwt_credentials"]["user_id"][0]
    api = config_data["api"]["host"]
    collection_cars = config_data["mongodb"]["collection_name"][1]
    user_name1 = config_data["jwt_credentials"]["user_name"][1]
    password1 = config_data["jwt_credentials"]["password"][1]
    user_id1 = config_data["jwt_credentials"]["user_id"][1]
    collection_film = config_data["mongodb"]["collection_name"][2]
    print(collection_film)
    user_name2 = config_data["jwt_credentials"]["user_name"][2]
    password2 = config_data["jwt_credentials"]["password"][2]
    user_id2 = config_data["jwt_credentials"]["user_id"][2]
except FileNotFoundError as e:
    print("Config file not found. Please make sure the file 'app/config.yaml' exists.")

except json.JSONDecodeError as e:
    print("Error decoding the JSON data from the config file.")

except KeyError as e:
    print("Key not found in the config data.")
