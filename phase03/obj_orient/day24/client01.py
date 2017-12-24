#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/30 21:43
__author__ = "WangYx"

import socket

obj = socket.socket()
obj.connect(('127.0.0.1',8090))
inp = input("请输入你要下载的文件名字: ")
obj.send(bytes(inp + ".jpg",encoding="utf-8"))
file_size = str(obj.recv(1024),encoding="utf-8")
total_size = file_size
trans_size = 0
while True:
	with open("new.jpg","wb") as f:
		if total_size == trans_size:
			break
		data = obj.recv(1024)
		f.write(data)

obj.close()
