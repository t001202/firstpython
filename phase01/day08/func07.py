#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
"""函数动态参数
	如果函数有默认参数 要放到没有默认参数的后面
	一:如何传入动态参数  在参数前面加 : *a
	二:**a 也是动态参数 但是 必须传key=value样式的
"""
def sendMessage(*t):
	print(t)

# sendMessage({'a':'11','b':'22'},"aaa",123)
# sendMessage(123,type("123"),id(123))
def send(**a):
	print(a)
#send(k1=123,k2=456)

def message(*a,**aa):
	if a is not None and aa is not None:
		print(a)
		print(aa)
	elif a is not None and aa is None:
		print(a)
	elif a is None and aa is not None:
		print(aa)
	else:
		print("全部为空")
message(123)
#send(123)   #会报错

