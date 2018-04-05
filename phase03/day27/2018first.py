#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

print("我要开始学习Python,坚持下去")


class SqlPool:
	__instance = None

	@staticmethod
	def getInstance():
		if SqlPool.__instance is not None:
			return SqlPool.__instance
		else:
			SqlPool.__instance = SqlPool()
			return SqlPool.__instance
