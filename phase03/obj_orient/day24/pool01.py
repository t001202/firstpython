#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/29 21:00
__author__ = "WangYx"

class SqlPool:

	_instance = None

	def __init__(self):
		self.ip = "1,1,1,1"
		self.port = 3306

	@staticmethod
	def getInstance():
		if SqlPool._instance:
			return SqlPool._instance
		else:
			SqlPool._instance = SqlPool()
			return SqlPool._instance

	def getConnection(self):
		print("获取数据库连接")


for i in range(10):
	obj = SqlPool.getInstance()
	print(obj)