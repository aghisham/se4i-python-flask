from app import app
from flask import request, jsonify, render_template
from app.models.project_z import Project

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

@app.route("/home/")
def home_page():
    return render_template('index1.html')

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route("/hello")
def about():
    return render_template(f'templates/about.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route("/get-name")
def get_name():
    project = Project(thisdict)

    return jsonify({"name": project.get_name()})
