#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/23 22:30
__author__ = "WangYx"

class Foo:

	country = "China"

	def __init__(self,name):
		self.name = name

	@set
	def updateName(self,name):
		self.name = name

	@staticmethod
	def show():
		print("show")

	@property
	def func(self):
		temp = "%s sb" % self.name
		print(temp)
		return temp

	@classmethod
	def clsmethod(cls):
		print("cls")


per = Foo("alex")
country = Foo.country
print(country)
obj1 = Foo.func
print(obj1)
Foo.clsmethod()
Foo.show()
