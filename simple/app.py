import os

import tornado.ioloop
from tornado.options import define, options, parse_command_line
import tornado.web

import socketio
from sio import sio

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")

class MainHandler(tornado.web.RequestHandler):
  def get(self):
      self.render("index.html")

def main():
  parse_command_line()
  app = tornado.web.Application(
    [
      (r"/", MainHandler),
      (r"/socket.io/", socketio.get_tornado_handler(sio)),
    ],
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=options.debug,
  )
  app.listen(options.port)
  tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
