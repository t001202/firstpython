#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

# lambda
func = lambda x, y: x + y - 3
i = func(1, 5)


def func1(args):
	args()


def func2(args):
	print(args)

print(func1(func2))

filter()

