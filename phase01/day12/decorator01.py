#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"


def outer(func):
	"""
	装饰器
	:param func: 
	:return: 
	"""
	def inner():
		print("hello python")
		print("hello python")
		print("hello python")
		r = func()
		print("end")
		print("end")
		print("end")
		return r
	return inner


@outer
def f2():
	print("F2")
	return "000"
ret = f2()
print(ret)
