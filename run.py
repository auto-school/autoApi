from app import app
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app.app))
    http_server.listen(8181)
    IOLoop.instance().start()
