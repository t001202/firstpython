#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

str1 = "abc"
b = bytes(str1, encoding="gbk")
s = str(b,encoding="gbk")
print(type(b))
print(type(s))
