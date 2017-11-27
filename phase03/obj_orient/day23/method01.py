#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/26 23:55
__author__ = "WangYx"

'''
python 中面向对象  对象中的方法
__init__;__del__
__call__  : Django , python 
'''

class Foo:
	def __init__(self):
		print("__init__")

	def __call__(self, *args, **kwargs):
		print("call")

ret = Foo()()
