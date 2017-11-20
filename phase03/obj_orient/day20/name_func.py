#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/17 0:00
__author__ = "WangYx"

def get_formatted_name(first,last):
	"""进行名字格式化"""
	full_name = first +''+ last
	print(full_name)
	return full_name.title()