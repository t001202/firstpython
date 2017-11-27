#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/23 23:01
__author__ = "WangYx"

class Animal:

	country = "China"
	__country = "USA"

	def __init__(self, name):
		self.name = name

	def show(self):
		print("1: " + self.__country)

	def __getname(self):
		print(self.name)

print(Animal.country)
obj = Animal("alex")
print(obj.show())


class Cat(Animal):

	def showcat(self):
		print("cat")

obj2 = Cat()
