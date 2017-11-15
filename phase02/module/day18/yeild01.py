#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

def xrange():
	print("1")
	yield 11
	print("2")
	yield 22
	print("3")
	yield 33

r = xrange()
# print(r)
# print(r.__next__())

def range01(n):
	start = 0
	while True:
		if start > n:
			return
		yield start
		start += 1

# obj = range01(3)
# n1 = obj.__next__()
# n2 = obj.__next__()
# n3 = obj.__next__()
# n4 = obj.__next__()
# n5 = obj.__next__()
# print(n1,n2,n3,n4,n5)

# for i in range(1,100):
# 	if i % 2 == 0 or i % 3 == 0:
# 		print(i)
flag = isinstance("123", str)
# print(flag)
a = iter([1,2,3,4])
# for i in a:
# 	print(i)