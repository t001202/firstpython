#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/16 22:32
__author__ = "WangYx"


class person:
	def __init__(self, name, age, weight):
		self.name = name
		self.age = age
		self.weight = weight

	def eat(self):
		self.weight += 2

	def sport(self):
		self.weight -= 3


obj1 = person('李磊', 18, 100)
obj2 = person('韩梅梅', 18, 100)
person('小明', 18, 100)

# obj1.eat()
# print(obj1.weight)
# obj1.sport()
# print(obj1.weight)

import pickle
import os
log_file = str(obj2.name) + ".log"
flag = os.path.isfile(log_file)
# print(flag)
if flag:
	f = open(log_file, 'rb')
	# print(os.path.getsize(str(f.name)))
	if os.path.getsize(str(f.name)) != 0:
		ret = pickle.load(f)
		print(ret.weight)
	else:
		obj1.eat()
		obj1.eat()
		obj1.eat()
		obj1.eat()

		pickle.dump(obj2,open(log_file,'wb'))
	# os.close(log_file)
else:
	open(log_file,'w')
