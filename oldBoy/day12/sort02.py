#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
li = [11, 4, 23, 76, 35, 9, 19]
list


def __bubblingsort__(args):
	for i in range(len(args) - 1):
		# current_value = li[i]
		# next_value = li[i + 1]
		for j in range(len(args) - i - 1):
			if args[j] > args[j + 1]:
				temp = args[j]
				args[j] = args[j + 1]
				args[j + 1] = temp
	print(li)


__bubblingsort__(li)
