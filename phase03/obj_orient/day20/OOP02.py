#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"


class Dog():

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title() + " is now sitting")

	def updateName(self,name):
		self.name = name
new_dog = Dog("hily",19)
new_dog.updateName("cary")
new_dog.sit()