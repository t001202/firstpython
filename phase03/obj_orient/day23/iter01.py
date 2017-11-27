#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/27 21:13
__author__ = "WangYx"

class Foo:


	def __iter__(self):
		yield 1
		yield 2
		yield 3


obj = Foo()

for i in obj:
	print(i)
