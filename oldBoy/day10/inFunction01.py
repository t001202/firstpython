#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

# i = abs(-123)  #取绝对值
# print(i)
# li = [1,3]
# b= all(li)
# print(b)
class Foo:
	def __repr__(self):
		return "hello"

obj = Foo
r = ascii(obj)
# print(r)

num = int('0xe',base=16)
print(num)
print(chr(66))