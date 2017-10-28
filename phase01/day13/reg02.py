#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

def num(n):
	if n == 1000:
		return
	ret = n + 1
	print(ret)
	num(ret)

num(1)
