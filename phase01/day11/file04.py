#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

li = ['a', 'b', 'c']


def gethashcode(args):
	for i in args:
		hashnum = hash(i)
		return hashnum


filter(gethashcode,li)
print(li)
