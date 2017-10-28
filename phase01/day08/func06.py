#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
"""内置函数"""
"""函数的默认参数
   当不指定参数的时候  默认
   含有默认值的参数 放到后面
"""
def drive(name="李白"):
	temp = "\033[1;31;40m" + name + "\033[0m开车,去日本"
	print(temp)
drive("张三")
drive()