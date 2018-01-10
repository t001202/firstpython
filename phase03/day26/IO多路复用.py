#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/12/25 22:14
__author__ = "WangYx"
"""
	IO多路复用就是
"""
import socket

sk1 = socket.socket()
sk1.bind(('127.0.0.1', 8081))
sk1.listen()
#文件句柄
sk2 = socket.socket()
sk2.bind(('127.0.0.1', 8082))
sk2.listen()

sk3 = socket.socket()
sk3.bind(('127.0.0.1', 8083))
sk3.listen()

inputs = [sk1, sk2, sk3, ]
import select

while True:
	#内容自动监听  这两sk1 sk2 对象  当一个放生变化就会放到r_list 中
	r_list,w_list,e_list = select.select(inputs, [], [], 1)
	print("存放list: " + str(r_list))
# while True:
# 	conn, address = sk.accept()
# 	while True:
# 		conn_bytes = conn.recv(1024)
# 		conn_str = str(conn_bytes, encoding='utf-8')
# 		conn.sendall(bytes(conn_str, encoding='utf-8'))
# 	conn.close()
