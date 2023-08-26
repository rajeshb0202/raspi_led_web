from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from led import control_led

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('led_control.html')


@socketio.on('led_status')
def handle_led_status(message):
    status = message['data']
    control_led(status)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)