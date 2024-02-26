from flask import Flask, request
from flask_socketio import SocketIO, join_room, emit
from flask_cors import CORS

app = Flask(__name__)
# Allow all origins with CORS
CORS(app)
# Initialize SocketIO with CORS allowed for all origins
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/')
def index():
    pass

# TODO: Log a message to console that a user is connected
@socketio.on('connect')
def handle_connect():
    pass


# TODO: Log a message to console that a user is disconnected
@socketio.on('disconnect')
def handle_disconnect():
    pass

# TODO: Join a room
@socketio.on('joinRoom')
def handle_join_room(room_id):
    pass

# TODO: Use socket.io to emit the message to all connected clients
@socketio.on('chatMessage')
def handle_chat_message(message):
    pass


if __name__ == '__main__':
    # Use port 3000 or the one set in the 'PORT' environment variable
    socketio.run(app, host='0.0.0.0', port=3000, debug=True)
