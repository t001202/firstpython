#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/23 22:10
__author__ = "WangYx"

class Foo:

	country = "China"

	def __init__(self,name):
		self.name = name

	@staticmethod
	def show():
		print("show")

	@classmethod
	def selfcls(cls):
		print(cls)

Foo.show()
Foo.selfcls()
