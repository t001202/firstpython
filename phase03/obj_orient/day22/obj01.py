#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/22 21:48
__author__ = "WangYx"

'''面向对象进阶
   成员
   成员修饰符
'''


class B:
	def ooo(self):
		print("B.ooo")


class C(B):
	def xxx(self):
		print("B.xxx")

	def ooo(self):
		print("B.OOO")


class A:
	def ooo(self):
		print("A.ooo")


class D(A, C):
	pass


d1 = D()
d1.ooo()
