from flask import jsonify, Blueprint
from app.models.project import Project


controller_blueprint = Blueprint("controller_blueprint", __name__)


@controller_blueprint.route("/")
def home_page():
    return "hello from homepage"


@controller_blueprint.route("/about")
def about():
    return "about page is here"


@controller_blueprint.route("/get-name")
def get_name():
    project = Project("SE4I project")

    return jsonify({"name": project.get_name()})
