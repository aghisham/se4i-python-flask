from app import app
from flask import request, jsonify, render_template
from app.models.project_user import Project_user
import json


data = json.load(open('app/static/data_list.json'))
users_list = data if (len(data)) else []

@app.route("/home/")
def home_page():
    return render_template('index1.html')

@app.route('/projects/')
def projects():
    return 'The project page'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route("/get-dec")
def get_dec():
    project_user = Project_user(users_list)

    return jsonify({"dec": project_user.get_dec()})

@app.route("/cars", methods=["GET"])
def indexofcars():
    return jsonify(users_list)
