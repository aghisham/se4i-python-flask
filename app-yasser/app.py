from flask import Flask, Blueprint
import config
import controllers.HomeController as HomeController
import controllers.UserController as UserController

app = Flask(__name__)
view = Blueprint('view', __name__, template_folder='templates', static_folder='static', url_prefix='/')
api  = Blueprint('api', __name__, static_folder='static', url_prefix='/api')

# --------------------------------------- Routes --------------------------------
@view.route('/', methods=['GET'])
def index():
    return HomeController.index()


@api.route('/', methods=['GET'])
def api_index():
    return HomeController.api_index()


@view.route('/user', methods=['GET'])
def index_user():
    return UserController.index()


@api.route('/user', methods=['GET'])
def api_index_user():
    return UserController.api_index()


# --------------------------------------- Run App --------------------------------
app.register_blueprint(view)
app.register_blueprint(api)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=config.DEBUG)
