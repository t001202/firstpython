#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/12/25 22:33
__author__ = "WangYx"

import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8081))

obj_recv = obj.recv(1024)
obj_str = str(obj_recv, encoding='utf-8')
print(obj_str)

while True:
	inp = input("请输入发送的内容: ")
	if inp == 'q':
		obj.sendall(bytes(inp, encoding='utf-8'))
		break
	else:
		obj.sendall(bytes(inp, encoding='utf-8'))
