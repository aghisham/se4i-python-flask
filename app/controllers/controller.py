from app import app
from flask import request, jsonify, render_template
from app.models.project import Project


@app.route("/")
def homepage():
    return render_template(f'templates/index.html')


@app.route("/about")
def about():
    return render_template(f'templates/about.html')


@app.route("/get-name")
def get_name():
    project = Project("SE4I project")

    return jsonify({"name": project.get_name()}) 
