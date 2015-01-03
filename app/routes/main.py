import tornado.template
from .base import BaseHandler


class MainHandler(BaseHandler):
	def get(self):
		print(self.request)
		self.write("Hello")