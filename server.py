from app import app
# from app import socketio

app.run(host="0.0.0.0", use_reloader=True, port=8080)
# socketio.run(app, host="0.0.0.0", port=8080, use_reloader=True)
