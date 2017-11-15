#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import commons as comm

f_ = comm.f1()
# print(f_)
pro = input("请输入: ")
# print(pro,type(pro))
dd = __import__(pro)
new_func = input("请输入要执行的函数: ")
attr_func = getattr(dd, 'NAME')
print(attr_func)
# ret = attr_func()
# print(ret)
# dd_f_ = dd.f2()
# print(dd_f_)