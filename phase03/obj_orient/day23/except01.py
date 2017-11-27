#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/27 22:04
__author__ = "WangYx"

import logging
#
# inp = input("请输入数字:")
#
# try:
# 	raise Exception("信息出错...")
# 	num = int(inp)
# 	print(num)
# except Exception as e:
#
# 	logging.info(e)
# 	print(e)
# 	print("输入数据格式不正确")

class Foo:

	def __init__(self,name):
		self.xo = name

	# def __str__(self):
	# 	return self.xo

obj = Foo("error...")
print(obj)
print(Foo.__str__("000"))