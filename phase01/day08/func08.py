#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
"""函数动态参数: *  元组  元组的元组
				**  字典
	变量名  一般 *args ,** kwargs  
	为动态参数传入列表 字典 
"""
def method(*args):
	print(args,type(args))
li = [11,22,33,44]
li2 = (11,22,33,44)

def method2(**kwargs):
	print(kwargs,type(kwargs))
dic = {"key":123}
method2(**dic)
method(dic)
# method(li)
# method(*li)

