#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"


def f1():
	return "f1"


def f2():
	ret = f1();
	return ret


def f3():
	ret = f2()
	return ret

ret = f3()
print(ret)
