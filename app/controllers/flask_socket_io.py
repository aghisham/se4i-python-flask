""""Import python packages to work with API."""
from flask import render_template, jsonify
from app import app, socketio


# List to store sent messages
sent_messages = []


@app.route("/api/flask_socketio")
def socket():
    """Route to render the Flask-SocketIO HTML page."""
    return render_template("flask_socketio.html")


@app.route("/api/messages")
def get_sent_messages():
    """Route to get all sent messages in JSON format."""
    return jsonify(sent_messages)


@socketio.on("connect")
def handle_connect():
    """Event handler for client connection."""
    print("Client connected")

    # Send all the sent messages to the newly connected client
    socketio.emit("all_messages", sent_messages)


@socketio.on("disconnect")
def handle_disconnect():
    """Event handler for client disconnection."""
    print("Client disconnected")


@socketio.on("message")
def handle_message(data):
    """Event handler for receiving messages from the client."""
    print("Received message:", data)
    sent_messages.append(data)
    socketio.emit("response", data)
    socketio.emit("all_messages", sent_messages)
