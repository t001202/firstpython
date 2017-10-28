#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"


def recursion(a1, a2):
	"""
	斐波那契数列
	:param a1: 
	:param a2: 
	:return: 
	"""
	print(a1,end="\t")
	if a1 > 10000:
		return
	a3 = a1 + a2
	recursion(a2, a3)


recursion(0,1)
