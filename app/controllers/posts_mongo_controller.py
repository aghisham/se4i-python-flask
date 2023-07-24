from flask import Flask, request, jsonify
from bson.objectid import ObjectId
from app import app
from app.models.mongo_singleton import MongoDBSingleton
import requests
import json
from bson import json_util

API_BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# Singleton MongoDB connection instance for database 'se4i' and collection 'posts' with a custom MongoDB URL
custom_mongo_url = 'mongodb://localhost:27017/'
mongo_singleton = MongoDBSingleton(mongo_url=custom_mongo_url, database_name='se4idata', collection_name='posts')
# Routes for CRUD operations
print(mongo_singleton.get_collection())

# Controller: Insert data from API into MongoDB
@app.route("/api/store", methods=["GET"])
def store_data():
    response = requests.get(API_BASE_URL)
    if response.status_code == 200:
        api_data = response.json()
        json_data = json.loads(json_util.dumps(api_data))  # Convert the ObjectId objects to strings
        inserted_ids = mongo_singleton.get_collection().insert_many(json_data).inserted_ids
        # Convert the inserted_ids to strings as well to avoid serialization issues
        inserted_ids = [str(id) for id in inserted_ids]
        return jsonify({"message": "Data inserted successfully", "inserted_ids": inserted_ids})
    else:
        return jsonify({"message": "Failed to fetch data from the API"}), response.status_code



# Create a new post
@app.route('/api/posts', methods=['POST'])
def create_post_mongo():
    data = request.get_json()
    try:
        collection = mongo_singleton.get_collection()
        # Insert the data into the collection
        post_id = collection.insert_one(data).inserted_id
        return jsonify({'success': True, 'message': 'Post created successfully', 'post_id': str(post_id)})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Read all posts
@app.route('/api/posts', methods=['GET'])
def get_all_posts_mongo():
    try:
        collection = mongo_singleton.get_collection()
        posts = list(collection.find({}))
        for post in posts:
            post['_id'] = str(post['_id'])
        return jsonify({'success': True, 'data': posts})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Read a specific post by ID
@app.route('/api/posts/<post_id>', methods=['GET'])
def get_post_mongo(post_id):
    try:
        collection = mongo_singleton.get_collection()
        post = collection.find_one({'_id': ObjectId(post_id)})
        if post:
            post['_id'] = str(post['_id'])
            return jsonify({'success': True, 'data': post})
        else:
            return jsonify({'success': False, 'message': 'Post not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Update a post by ID
@app.route('/api/posts/<post_id>', methods=['PUT'])
def update_post_mongo(post_id):
    data = request.get_json()
    try:
        collection = mongo_singleton.get_collection()
        # Update the post in the collection
        result = collection.update_one({'_id': ObjectId(post_id)}, {'$set': data})
        if result.modified_count == 1:
            return jsonify({'success': True, 'message': 'Post updated successfully'})
        else:
            return jsonify({'success': False, 'message': 'Post not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Delete a post by ID
@app.route('/api/posts/<post_id>', methods=['DELETE'])
def delete_post_mongo(post_id):
    try:
        collection = mongo_singleton.get_collection()
        # Delete the post from the collection
        result = collection.delete_one({'_id': ObjectId(post_id)})
        if result.deleted_count == 1:
            return jsonify({'success': True, 'message': 'Post deleted successfully'})
        else:
            return jsonify({'success': False, 'message': 'Post not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


