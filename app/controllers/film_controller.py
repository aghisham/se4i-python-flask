import json
from flask import request, jsonify, render_template, Blueprint
from bson import ObjectId
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import Schema, fields
from app.models.mongo_singleton import MongoDBSingleton
from app.config import database_name, collection_film, mongodb_host, port
from app import app, DOCS


data = json.load(open("app/static/films.json"))
films_list = data

db_connector = MongoDBSingleton(
    mongo_url=mongodb_host + "/" + str(port),
    database_name=database_name,
    collection_name=collection_film,
)

film_blueprint = Blueprint(
    "film_blueprint",
    __name__,
)


class StringResponseSchema(Schema):
    """Default Response Schema"""

    message = fields.Str()


@film_blueprint.route("", provide_automatic_options=False)
@doc(description="get films", tags=["Filmes"])
def index():
    """index"""
    return render_template("filmIndex.html")


@film_blueprint.route("/save", methods=["GET"], provide_automatic_options=False)
@doc(description="get films", tags=["Filmes"])
@marshal_with(StringResponseSchema())
def store_films():
    """save data to DB"""
    try:
        coll = db_connector.get_collection()
        coll.insert_many(data)
        return {"message": "data imported"}, 200
    except Exception as e:
        return {"message": str(e)}, 500


@film_blueprint.route("/<title>", methods=["GET"], provide_automatic_options=False)
@doc(description="get films", tags=["Filmes"])
def add(title):
    """get film by title"""
    try:
        existed_coll = db_connector.get_collection()
        film = existed_coll.find_one({"Title": title})
        if film:
            film["_id"] = str(film["_id"])
            return {"data": film}
        else:
            return jsonify({"message": "Film not found"}), 404
    except Exception as e:
        return jsonify({"message": "fail"}), 400


@film_blueprint.route("", methods=["GET"])
@doc(description="get films", tags=["Filmes"])
def display():
    """get all films in DB"""
    try:
        existed_coll = db_connector.get_collection()
        films = list(existed_coll.find({}))
        for film in films:
            film["_id"] = str(film["_id"])
        return jsonify({"success": True, "data": films})
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@film_blueprint.route("", methods=["POST"])
@doc(description="get films", tags=["Filmes"])
def create_film():
    """create film"""
    data_to_create = request.get_json()
    try:
        existed_coll = db_connector.get_collection()
        id_created = existed_coll.insert_one(data_to_create).inserted_id
        return (
            jsonify(
                {
                    "success": True,
                    "message": "Film created successfully",
                    "post_id": str(id_created),
                }
            ),
            200,
        )

    except Exception as e:
        return jsonify({"message": str(e)}), 500


@film_blueprint.route("/<title>", methods=["PUT"])
@doc(description="get films", tags=["Filmes"])
def update_film(title):
    """update film by title"""
    try:
        data = request.get_json()
        existed_coll = db_connector.get_collection()
        film = existed_coll.find_one({"Title": title})
        if film:
            existed_coll.update_one(
                {"_id": ObjectId(film["_id"])}, {"$set": data})
            return {"success": True, "message": "Film is updated successfully"}, 200
        else:
            return {"success": False, "message": "Film is Not Found"}, 404
    except Exception as e:
        return {"success": False, "message": str(e)}, 500


@film_blueprint.route("/<title>", methods=["DELETE"])
@doc(description="get films", tags=["Filmes"])
def delete_film(title):
    """delete film by title"""
    try:
        existed_coll = db_connector.get_collection()
        film = existed_coll.find_one({"Title": title})

        if film:
            del_result = existed_coll.delete_one({"Title": title})
            if del_result.deleted_count == 1:
                return {"success": True, "message": "Film is deleted"}, 200
            else:
                return {"success": False, "message": "Film is Not Found"}, 404
        else:
            return {"success": False, "message": "Film is Not Found"}, 404
    except Exception as e:
        return {"success": False, "message": str(e)}


app.register_blueprint(film_blueprint, url_prefix="/films")
DOCS.register(index, blueprint="film_blueprint")
DOCS.register(store_films, blueprint="film_blueprint")
