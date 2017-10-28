#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"


def func01(args):
	if args > 200:
		return True
	else:
		return False


li = list()
li.append(147)
li.append(123)

for i in filter(func01, [123,456,789]):
	print(i)
