from app import app
from flask import request, jsonify, render_template, Blueprint
from app.models.mongo_singleton import MongoDBSingleton
from app.config import mongodb_host, port, database_name, collection_film
from bson import ObjectId
import json

data = json.load(open("app/static/films.json"))
films_list = data

db_connector = MongoDBSingleton(
    mongo_url=mongodb_host + "/" + str(port),
    database_name=database_name,
    collection_name=collection_film,
)
0

film_blueprint = Blueprint('film_blueprint', __name__,)


@film_blueprint.route("/")
def index():
    return render_template("filmIndex.html")


# save data to DB
@film_blueprint.route("/films/save", methods=["GET"])
def store_films():
    try:
        coll = db_connector.get_collection()
        coll.insert_many(data)
        return "data imported", 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# get film by title
@film_blueprint.route("/films/<title>", methods=["GET"])
def add(title):
    try:
        existed_coll = db_connector.get_collection()
        film = existed_coll.find_one({"Title": title})
        if film:
            film["_id"] = str(film["_id"])
            return {"success": True, "data": film}
        else:
            return jsonify({"success": False, "message": "Film not found"}), 404
    except Exception as e:
        return jsonify({"message": "fail"}), 400


# get all films in DB
@film_blueprint.route("/films", methods=["GET"])
def display():
    try:
        existed_coll = db_connector.get_collection()
        films = list(existed_coll.find({}))
        for film in films:
            film["_id"] = str(film["_id"])
        return jsonify({"success": True, "data": films})
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# create film
@film_blueprint.route("/films", methods=["POST"])
def create_film():
    data_to_create = request.get_json()
    try:
        existed_coll = db_connector.get_collection()
        id_created = existed_coll.insert_one(data_to_create).inserted_id
        return jsonify(
            {
                "success": True,
                "message": "Film created successfully",
                "post_id": str(id_created),
            }
        ), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500


# update film by title
@film_blueprint.route("/films/<title>", methods=["PUT"])
def update_film(title):
    try:
        data = request.get_json()
        existed_coll = db_connector.get_collection()
        film = existed_coll.find_one({"Title": title})
        if film:
            existed_coll.update_one({"_id": ObjectId(film["_id"])}, {"$set": data})
            return {"success": True, "message": "Film is updated successfully"}, 200
        else:
            return {"success": False, "message": "Film is Not Found"}, 404
    except Exception as e:
        return {"success": False, "message": str(e)}, 500


# delete film by title
@film_blueprint.route("/films/<title>", methods=["DELETE"])
def delete_film(title):
    try:
        existed_coll = db_connector.get_collection()
        film = existed_coll.find_one({"Title": title})

        if film:
            del_result = existed_coll.delete_one({"Title": title})
            if del_result.deleted_count == 1:
                return (
                    {"success": True, "message": "Film is deleted"}, 200
                )
            else:
                return (
                    {"success": False, "message": "Film is Not Found"}, 404
                )
        else:
            return {"success": False, "message": "Film is Not Found"}, 404
    except Exception as e:
        return {"success": False, "message": str(e)}


app.register_blueprint(film_blueprint)
