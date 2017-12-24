#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/29 21:26
__author__ = "WangYx"

from wsgiref.simple_server import  make_server

def RunServer(environ,start_response):
	start_response(status="200 OK",headers=[('Content-Type','text/html')])
	url = environ['PATH_INFO']
	print(url)
	return "OLD_BOY"

if __name__ == "__main__":
	httpd = make_server('',8008,RunServer)
	print("Serving Http on port 8008...")
	httpd.serve_forever()

status="200 OK"
ret = status.split(" ", 1)[0]
print(ret)
