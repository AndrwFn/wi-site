import os.path, re, tornado.httpserver, tornado.ioloop, tornado.web
from tornado.options import define, options
import hashlib
from routes.main import MainHandler


class WiSiteApplication(tornado.web.Application):
	def __init__(self):
		handlers = [
			('/', MainHandler)
		]
		settings = dict(
			template_path=os.path.join(os.path.dirname(__file__), "templates"),
			static_path=os.path.join(os.path.dirname(__file__), "static"),
			debug=True,
			xsrf_cookies = False,
			cookie_secret = str(hashlib.sha224(os.urandom(100)).hexdigest()))

		tornado.web.Application.__init__(self, handlers, **settings)

def run_instance(port):
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(WiSiteApplication())
	http_server.listen(port)
	print("Server started on port %s" % port)
	tornado.ioloop.IOLoop.instance().start()
