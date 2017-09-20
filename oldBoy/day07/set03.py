#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

#set 的方法功能 intersection isdisjoint   issubset
se = set([11,22,33])
be = set([11,44,55])
be1 = set([66])
be2 = set([11,22])
de = se.intersection(be)
print(de)
flag = se.isdisjoint(be1)  #判断是否 有交集
print(flag)
m = se.issubset(be2)
print(m)

ret = se.pop()
print(ret)
print(se)

