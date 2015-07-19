from gevent import monkey
from flask import Flask, Response, render_template, request
from socketio import socketio_manage
from socketio.namespace import BaseNamespace

monkey.patch_all()

app = Flask(__name__)
app.debug = True
app.config['PORT'] = 5000

@app.route('/', methods=['GET'])
def loading():
    return render_template('landing.html')

@app.route('/chat/<path:remaining>')
def socketio(remaining):
    try:
        socketio_manage(request.environ, {'/chat': ChatNamespace}, request)
    except:
        app.logger.error("Exception while socket connection", exc_info=True)

    return Response()

class ChatNamespace(BaseNamespace):
    def initialize(self):
        self.logger = app.logger
        self.log("Socketio session started")

    def log(self, message):
        self.logger.info("[%s] %s" % (self.socket.sessid, message))

    def recv_connect(self):
        self.log("New connection")

    def recv_disconnect(self):
        self.log("Client disconnected")


