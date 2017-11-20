#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"


class Pig:


	def func01(self):
		print(self.say)

	def func02(self):
		print(self.sit)

pfun = Pig()
pfun.say = "你好"
pfun.sit = "坐下"
pfun.func01()
pfun.func02()
