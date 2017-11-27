#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/27 21:29
__author__ = "WangYx"

class Foo:
	"""
	明明你也很爱我
	"""

	def __init__(self):
		pass

	def __getitem__(self, item):
		print("item")

	def __setitem__(self, key, value):

		print("key")

	def __delitem__(self, key):

		print("del")

	def __call__(self, *args, **kwargs):

		print("call")

	def __iter__(self):
		yield 1
		yield 2
		yield 3


# obj = Foo()
#
# print(obj.__doc__)


class MyType(type):

	def __init__(self,whate,bases=None,dict=None):
		super(MyType,self).__init__(whate,bases,dict)

	def __call__(self, *args, **kwargs):
		obj = self.__new__(self,*args,**kwargs)

		self.__init__(obj)

class FFoo(object):
	__metaclass = MyType

	def __init__(self,name):
		self.name = name

	def __new__(cls, *args, **kwargs):
		return object.__new__(cls,*args,**kwargs)

obj = FFoo()
