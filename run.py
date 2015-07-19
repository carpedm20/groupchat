from groupchat import app
from gevent import monkey
from socketio.server import SocketIOServer

monkey.patch_all()

if __name__ == '__main__':
    SocketIOServer(
        ('', app.config['PROT']),
        app,
        resource='socket.io').serve_forever()
