#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/12/4 21:24
__author__ = "WangYx"

import socketserver
from tornado import ioloop as ilp
from tornado import web

class MainHandler(web.RequestHandler):
	def get(self):
		self.write("hello world")

application = web.Application([

	(r"/",MainHandler),
])

if __name__ == "__main__":
	application.listen(8888)
	ilp.IOLoop.instance().start()


# class MyServer(socketserver.BaseRequestHandler):
#
# 	def handle(self):
# 		conn = self.request
# 		conn.sendall()
# 		while True:
# 			conn.recv(1024)
#
#
# if __name__ == "__main__":
# 	server = socketserver.ThreadingTCPServer(("127.0.0.1",8090),MyServer)
# 	server.serve_forever()


