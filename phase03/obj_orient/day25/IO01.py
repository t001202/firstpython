#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/12/7 22:40
__author__ = "WangYx"

# IO 多路复用 >>>  可以监听多个文件描述符(socket对象) 一旦文件符发生变化  就可以感知到

import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8090))
sk.listen()

while True:
	conn,address = sk.accept()
	conn_bytes = conn.recv(1024)
	conn_str = str(conn_bytes,encoding="utf-8")
	conn.sendall(bytes(conn_bytes+" yes",encoding="utf-8"))

