from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from app import app, socketio


# List to store sent messages
sent_messages = []

@app.route("/api/flask_socketio")
def socket():
    return render_template("flask_socketio.html")

@app.route('/api/messages')
def get_sent_messages():
    return jsonify(sent_messages)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

    # Send all the sent messages to the newly connected client
    socketio.emit('all_messages', sent_messages)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    print('Received message:', data)
    sent_messages.append(data)
    socketio.emit('response', data)
    socketio.emit('all_messages', sent_messages)









