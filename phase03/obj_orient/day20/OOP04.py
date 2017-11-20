#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

# __init__  初始化方法  python解释器相当于java的虚拟机
# __del__  析构方法 python解释器在销毁对象时  自动执行
class Foo:
	def __init__(self):
		self.name = 'NAME'
		self.age = 18

obj = Foo()
print(obj.name, "\n" + str(obj.age))