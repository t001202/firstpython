#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

def outer(func):
	def inner(*arg, **kwargs):
		print("数据库的操作")
		ret = func(*arg, *kwargs)
		print(ret)
		print("将查询到的数据封装到bean对象中")

	# print("123")
	# ret = func(a1, a2)
	# print("456")
	# return ret
	return inner


@outer
def f1(a1, a2):
	print("ok")
	return a1 + a2


f1(1, 2)
