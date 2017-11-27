#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/22 22:14
__author__ = "WangYx"

'''python中对于构造方法的两种继承方式:
	super(派生类,self).__init__()
	基类.__init__(self)
'''

class animal:

	def __init__(self):
		print("animal 的构造方法")
		self.ty = "动物"

class Cat(animal):

	def __init__(self):
		print("cat 的构造方法")
		self.name = "猫"
		# super(Cat,self).__init__()
		animal.__init__(self)


cat = Cat()
print(cat.__dict__)
