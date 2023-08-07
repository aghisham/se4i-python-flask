import requests
import json
from flask import jsonify
from bson.objectid import ObjectId
from bson import json_util
from app import app
from app.models.mongo_singleton import MongoDBSingleton
from app.config import mongodb_host, port, database_name, collection_name, api


API_BASE_URL = api

# Singleton MongoDB connection instance for database 'se4i' and collection 'posts' with a custom MongoDB URL
custom_mongo_url = mongodb_host + f":{port}/"
mongo_singleton = MongoDBSingleton(
    mongo_url=custom_mongo_url,
    database_name=database_name,
    collection_name=collection_name,
)
# Routes for CRUD operations


@app.route("/datas/save", methods=["GET"])
def show_data():
    """Controller: Insert data from API into MongoDB"""
    response = requests.get(API_BASE_URL)
    if response.status_code == 200:
        show_data = response.json()
        json_data = json.loads(
            json_util.dumps(show_data)
        )  # Convert the ObjectId objects to strings
        inserted_ids = (
            mongo_singleton.get_collection().insert_many(json_data).inserted_ids
        )
        # Convert the inserted_ids to strings as well to avoid serialization issues
        inserted_ids = [str(id) for id in inserted_ids]
        return jsonify(
            {"message": "Data inserted successfully", "inserted_ids": inserted_ids}
        )
    else:
        return (
            jsonify({"message": "Failed to fetch data from the API"}),
            response.status_code,
        )


@app.route("/datas/store", methods=["GET"])
def get_all_datas_mongo():
    """Read all datas"""
    try:
        collection = mongo_singleton.get_collection()
        posts = list(collection.find({}))
        for post in posts:
            post["_id"] = str(post["_id"])
        return jsonify({"success": True, "data": posts})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/datas/store/<post_id>", methods=["GET"])
def get_data_mongo(post_id):
    """Read a specific data by ID"""
    try:
        collection = mongo_singleton.get_collection()
        post = collection.find_one({"_id": ObjectId(post_id)})
        if post:
            post["_id"] = str(post["_id"])
            return jsonify({"success": True, "data": post})
        else:
            return jsonify({"success": False, "message": "Post not found"}), 404
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
