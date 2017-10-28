#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
import random
#生成一个随机数,将数字转换成字母

# li = list()
# while len(li) < 4 :
# 	num = random.randrange(65, 90)
# 	# print(num)
# 	li.append(chr(num))
# for i in li:
# 	print(i,end="")

temp = ""
for i in range(6):
	radnum = random.randrange(0, 4)
	if radnum == 3 or radnum == 1:
		temp += str(random.randrange(0,10))
	else:
		temp += chr(random.randrange(65,91))

print(temp)
