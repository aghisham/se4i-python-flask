from flask import Flask
from flask_cors import CORS
import uuid
import datetime
import app.config as conf

# from flask_jwt import JWT # ------ uncomment if python version <= 3.9
from app.controllers.files_controller import files_bp
from app.controllers.user_controller import users_bp


app = Flask(__name__)
app.config["SECRET_KEY"] = uuid.uuid4().hex
app.config["JWT_EXPERATION_DELTA"] = datetime.timedelta(days=2)
app.config["JWT_AUTH_URL_RULE"] = "/auth"


CORS(app, resources={r"/": {"origins": "localhost:*"}})
# JWT(app=app, authentication_handler=conf.authenticate, identity_handler=conf.identity) # ------ uncomment if python version <= 3.9


# Register Blueprints
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(files_bp, url_prefix="/upload")


from app.controllers import (
    controller,
    controller_user,
    film_controller,
    item_controller,
    jwt_controller,
)
