#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/30 22:55
__author__ = "WangYx"

import socket
import os

sk = socket.socket()

sk.bind(('127.0.0.1',8090))
sk.listen(5)
while True:

	conn,address = sk.accept()
	sk.send(bytes("欢迎登录...",encoding="utf-8"),address)
	file_name = str(sk.recv(1024), encoding="utf-8")
	file_size = os.stat(file_name).st_size
	print(file_size)
	total_size = int(file_size)
	has_size = 0
	sk.sendall(bytes(str(file_size), encoding="utf-8"))
	with open(file_name,"wb") as f:
		for line in f:
			sk.sendall(bytes(line,encoding="utf-8"))





