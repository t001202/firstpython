#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/27 0:02
__author__ = "WangYx"

class Foo:
	"""
	我是以个注释
	"""
	def __init__(self):
		self.name = "alex"
		pass

	def __getitem__(self, item):

		print(item,type(item),"__getitem__")

	def __call__(self, *args, **kwargs):
		print("call")

	def __delitem__(self, key):
		print(key)

r = Foo()

print(r.__dict__)
print(Foo.__dict__)