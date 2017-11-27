#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/23 22:48
__author__ = "WangYx"

class Foo:

	def __init__(self,name):
		self.name = name

	@property
	def end(self):
		temp = self.name
		return temp

	@end.setter
	def end(self,value):
		self.name = value



obj = Foo("alex")
print(obj.end)
obj.end = "wpq"
print(obj.end)
