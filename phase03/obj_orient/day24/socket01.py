#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/30 21:11
__author__ = "WangYx"
#Socket(TCP IP)

import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9999))
sk.listen(5)
print("开始连接...")
while True:
	conn,address = sk.accept() # 接收连接和客户端地址
	conn.sendall(bytes("欢迎致电...",encoding='utf-8'))
	print(conn,address)
