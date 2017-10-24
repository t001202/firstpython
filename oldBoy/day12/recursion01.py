#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"


def f4(a, b):
	if a > 10:
		return
	c = a * b
	print(c)
	f4(b, c)


# ret = f4(1, 2)


def fibooneseq(depth, a1, a2):
	if depth == 10:
		return a1
	a3 = a1 + a2
	r = fibooneseq(depth + 1, a2, a3)
	return r


ret = fibooneseq(1, 0, 1)
print(ret)
