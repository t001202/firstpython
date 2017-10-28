#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
"""内置函数"""
"""def 函数名(形式参数)
		函数体
		:return "返回值"
	"""
def add(a,b,c):
	return a+b-c;

print(add(10,1,9))
print(add(a=1,b=2,c=4))  #可以指定形式参数  不需要按照顺序 就可以
