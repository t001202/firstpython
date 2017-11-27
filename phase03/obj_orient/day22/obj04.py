#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/22 22:44
__author__ = "WangYx"

class Foo:

	def __init__(self,name):
		self.name = name


	def show(self):
		print(" show")

# obj1 = Foo('alex')
# obj1.show()
obj = Foo("alex")

r = hasattr(Foo,'name')
print(r)

r = hasattr(obj,'name')
name = getattr(obj,'name')
print(name)
r = hasattr(obj,'show')
print(r)