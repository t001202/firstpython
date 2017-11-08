#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import random
flag = True
while flag:
	input_num = input("请输入数字: ")
	num = random.randrange(1,100)
	if num != input_num:
		print("您输入的数字不对!")
		continue
	else:
		flag = False

