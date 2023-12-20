from flask import (
        Flask, 
        request, 
        jsonify, 
        send_from_directory)
from flask_socketio import SocketIO, emit
import logging
import json

app = Flask(__name__, 
            template_folder='.', 
            static_folder='.',
            static_url_path='')

socketio = SocketIO(app)

@app.route('/health')
def health():
    return 'ok'

@app.route('/')
def test():
    return send_from_directory('./', 'index.html')

@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
    socketio.run(app, debug=True, use_reloader=False)
