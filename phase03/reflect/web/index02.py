#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

from phase03.reflect.day19 import commons as comm
from phase03.reflect.web import account as ac
import os

ac_path = os.path.isfile(ac)
print(ac_path)

new_module = input("请输入url: ")

module_inp, method_inp = new_module.split("/")
# pth = os.path.abspath(module_inp)
# print(pth)

if hasattr(module_inp, method_inp):
	met = getattr(module_inp, method_inp)
	ret = met()
	print(ret)
else:
	print("404")
