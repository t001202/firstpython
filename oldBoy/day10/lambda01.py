#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
"""简单的函数  lambda"""
def f1():
	return 123

f2 = lambda : 123

f3 = lambda a1,a2:a1+a2
r2 = f2()
r3 = f3(1,2)
print(r2)

