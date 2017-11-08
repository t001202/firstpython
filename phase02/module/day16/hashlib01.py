#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
import hashlib

hashlib_sha = hashlib.md5()
username = input("请输入用户名: \n")
hashlib_sha.update(bytes(username,encoding="utf-8"))
print("您的sha384加密后为: "+ "\033[5;31;47m" + hashlib_sha.hexdigest() + "\033[0m")

print('\033[1;31;40m')
# hash = hashlib.md5()
# hash.update(bytes('123',encoding="utf-8"))
# print(hash.hexdigest())
import sys
# import os
# ret = os.environ
# for i in ret.items():
# 	print(i[0],i[1])
# print("---------------------------")
# if os.name.lower() == "nt":
# 	print("您的系统为: windows")
# elif os.name.lower() == "ios":
# 	print("Ios")