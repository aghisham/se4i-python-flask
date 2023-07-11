from app import app
from flask import request, jsonify, render_template
from app.models.user import User


@app.route("/")
def homepage():
    return render_template(f'templates/index.html')


@app.route("/about")
def about():
    return render_template(f'templates/about.html')


@app.route("/get-name")
def get_name():
    user = User("SE4I project")

    return jsonify({"name": user.get_name()})
