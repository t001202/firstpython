#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"


def f1(*args,**kwargs):
	print(args)
	print(kwargs)

f1(1,2,3,5,6,9,8,k=123)
