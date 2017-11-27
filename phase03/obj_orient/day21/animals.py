#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/22 20:16
__author__ = "WangYx"


class Animals:

	def __init__(self,name):
		self.name = name

	def eating(self):
		print("eating")

	def drinking(self):
		print("drinking")

class Bird:

	def fly(self):
		print("flying")

class Cat(Animals,Bird):

	def jiao(self):
		print(self.name + "喵喵叫")


class Dog(Animals):

	def jiao(self):
		print(self.name + "汪汪叫")

class girl(Cat):

	def shopping(self):
		print(self.name + "购物")

