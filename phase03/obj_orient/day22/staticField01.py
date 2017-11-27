#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/23 21:20
__author__ = "WangYx"


class Provice:
	country = "China"

	def __init__(self, name):
		self.name = name

	# self.country = "中国"

	# self 表示对象本身

	@staticmethod
	def show():
		print("show")


hebei = Provice("河北")
henan = Provice("河南")
henan.show()
Provice.show()

country = Provice.country
print(country)


