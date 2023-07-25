from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
import app.config as conf


MODE = "development" # development - testing - production


# ------ Init App
app = Flask(__name__)
app.config.from_object(conf.config[MODE])
CORS(app, resources={r"/": {"origins": "localhost:*"}})
# ------ (JWT) uncomment if python version <= 3.9
# from app.controllers import authController

# ------ Init DB
DB = PyMongo(app).db


# ------ Register Blueprints
from app.controllers.user_controller import users_bp
app.register_blueprint(users_bp, url_prefix="/users")

from app.controllers.files_controller import files_bp
app.register_blueprint(files_bp, url_prefix="/upload")

from app.controllers.controller import controller_blueprint
app.register_blueprint(controller_blueprint, url_prefix="/controller")


from app.controllers import (
    controller,
    controller_user,
    film_controller,
    item_controller,
    jwt_controller,
    posts_mongo_controller,
)
