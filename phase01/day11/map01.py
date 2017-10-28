#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

li = [11, 22, 33]


def func1(args):
	return args + 100


r = map(func1, li)
for i in r:
	print(i)


def MyMap(func, args):
	result = []
	for i in args:
		ret = func(i)
		result.append(ret)
	return result


ret = MyMap(func1, li)
for re in ret:
	print(re)
