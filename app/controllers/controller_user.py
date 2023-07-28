from app import app
from flask import request, jsonify, render_template
from app.models.project_user import Project_user
import json
import requests


datas = json.load(open('app/static/data_list.json'))
users_list = datas if (len(datas)) else []

@app.route("/home/")
def home_page():
    return render_template('index1.html')

@app.route('/projects/')
def projects():
    return 'The project page'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route("/data/<int:id>", methods=["GET"])
def get_data(id):
    response = requests.get(f"data/{id}")
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "Data not found"}), response.status_code
    
@app.route("/get-dec")
def get_dec():
    project_user = Project_user(users_list)

    return jsonify({"dec": project_user.get_dec()})

@app.route("/data/1", methods=["GET"])
def indexofcars():
    return jsonify(users_list)
