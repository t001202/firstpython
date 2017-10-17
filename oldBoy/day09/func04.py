#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

def func4(args):
	for i in range(len(args)):
		if (i+1) % 2 == 1:
			print(args[i])

li = [11,22,33,44]
func4(li)
