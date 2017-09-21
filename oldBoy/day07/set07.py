#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by WangYx on 2017/9/21.
__author__ = "WangYx"
"""数据类型在内存中的存储方式"""
"""相当于链表  记录上一个数据的地址和下一个数据的地址"""
"""如java中的数组 个数是不能变的"""
"""深拷贝和浅拷贝:只要是拷贝  字符串和数字的id  都是一样的"""

import copy
# n1 = 123
# print(id(n1))
# n2 = copy.copy(n1)
# print(id(n2))
# n3 = n1
# print(id(n3))
n4 = {"k1":"wu","k2":123,"k3":["alex",456]}
n5 = copy.deepcopy(n4)
print(id(n4["k3"][1]))
print(id(n5["k3"][1]))