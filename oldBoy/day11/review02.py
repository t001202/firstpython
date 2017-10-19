#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import getpass
import random

message = input("请输入用户名: ")
pw = getpass.getpass("请输入密码: ")


def veriCode():
	temp = ""
	while len(temp) <= 6:
		num = random.randrange(0, 4)
		if num == 1 or num == 4:
			temp += random.randrange(0, 9)
		else:
			temp += chr(random.randrange(65, 99))
	print(temp)


ranCode = veriCode()
veriCodeMessage = input("请输入验证: ")
if ranCode == veriCodeMessage:
	print("验证码不正确: ")
else:
	if message == "tom" and pw == "123":
		print("登录成功")
	else:
		print("用户名和密码不正确")
