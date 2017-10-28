#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

# temp = 'fhajfnjka'
# ret = isinstance(temp,str)
# print(ret)
def has_space(args):
	ret = True
	for c in args:
		if str(c).isspace():
			ret = False
			break
	return ret

# print(has_space("12 56"))

def lenRg2(args):
	if len(args) > 2:
		print(args[2:])
		del args[2:]
	else:
		return args
li2 = [11,22,33]
lenRg2(li2)
print(li2)


def addList(args):  #pyton中传值  传的是引用  直接修改参数
	args.append(123)
	pass

li = [11,22]
addList(li)
print(li)

