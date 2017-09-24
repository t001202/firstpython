#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
"""函数  面向过程的编程 频繁的复制粘贴
		 函数式编程  
         面向对象的编程  """
def func():
	print("hello world")
	print("hello world")
def error():
	print("失败了!!!")
num = 10
if num >= 11:
	func()
else:
	error()