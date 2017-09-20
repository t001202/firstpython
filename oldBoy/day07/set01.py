#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

s= set([11,22,33])  #无序不重复的集合
s.add(111)
s.add(222)
s.add(0)
s.clear()
print(s)
print(type(s))
