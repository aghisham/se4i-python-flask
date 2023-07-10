from flask import request, jsonify, render_template


def index():
    return render_template(f'templates/home/index.html')


def api_index():
    return jsonify({'message': 'Hello API'})
