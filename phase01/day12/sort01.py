#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

"""
  排序算法
"""


def changeNum(a, b):
	a = a + b
	b = a - b
	a = a - b
	return a,b


li = [11, 4, 23, 76, 35, 9, 19]

a = 123
b = 456

changeNum(a,b)

# a = a + b  # 579
# b = a - b  # 579-456
# a = a - b  # 579-123

print(a)
print(b)
