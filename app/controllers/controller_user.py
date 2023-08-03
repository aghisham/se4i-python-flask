<<<<<<< HEAD
from flask import Blueprint,request, jsonify, render_template
from app.models.project_user import Data,DataSchema
from app.models.user import DefaultResponseSchema
=======
from flask import Blueprint, request, jsonify, render_template
from app.models.project_user import (
    Project_user,
    Data,
    DataSchema,
)
import json
import requests
from bson.json_util import dumps
from flask_apispec import doc, use_kwargs, marshal_with
from app import app, DB, DOCS

#users_list = datas if (len(datas)) else []
#users = {user_name1: {"user_id": user_id1, "password": password1}}
datas_bp = Blueprint(
    "datas_bp", __name__, template_folder="templates", static_folder="static"
)


@datas_bp.route("", methods=["GET"], provide_automatic_options=False)
@doc(description="Get All Datas", tags=["Datas"])
@marshal_with(DataSchema(many=True))
def home_page():
    cursor = DB.datas.find({}).limit(20)
    return jsonify(dumps(cursor))


@app.route("/projects/")
def projects():
    return "The project page"

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404


@datas_bp.route("/<int:user_id>", methods=["GET"], provide_automatic_options=False)
@doc(description="Get User", tags=["Datas"])
@marshal_with(DataSchema(many=False))
def indexofcars(user_id):
    """Get user by id

    Args:
        id (int): user id

    Returns:
        dict: User
    """
    user = DB.datas.find_one({"id": user_id})  # type: ignore
    if user:
        return jsonify(dumps(user))
    return {"message": "Not existe"}, 400

<<<<<<< HEAD
@datas_bp.route("/update/<int:user_id>", methods=["PUT"], provide_automatic_options=False)
=======

@datas_bp.route("/data/<int:user_id>", methods=["PUT"], provide_automatic_options=False)
>>>>>>> 4928baf94275704aca5042d89e94695480bdb5a8
@doc(description="Update User", tags=["Datas"])
@use_kwargs(DataSchema, location="json")
@marshal_with(DefaultResponseSchema())
def update(data_id, **kwargs):
    try:
        if request.json:
            data_model = Data(
                data_id,
                request.json["brand"],
                request.json["model"],
                request.json["year"],
                request.json["des"],
            )
            data_model.update()
        return {"message": "success"}, 200
    except Exception:
        return {"message": "Not existe"}, 400

    
#@app.route("/get-dec")
#def get_dec():
   # project_user = Project_user(datas_bp)
=======

@app.route("/get-dec")
def get_dec():
    project_user = Project_user(datas_bp)
>>>>>>> 4928baf94275704aca5042d89e94695480bdb5a8

 #   return jsonify({"dec": project_user.})


app.register_blueprint(datas_bp, url_prefix="/datas")
DOCS.register(indexofcars, blueprint="datas_bp")
DOCS.register(update, blueprint="datas_bp")
DOCS.register(home_page, blueprint="datas_bp")
# DOCS.register(get_data, blueprint="datas_bp")
