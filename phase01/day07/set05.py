#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

old_dict = {
	"#1":11,
	"#2":22,
	"#3":100,
}
new_dict = {
	"#1":33,
	"#4":22,
	"#7":100,
}
old_set = set(old_dict)
new_set = set(new_dict)
# difference1 = old_set.difference(new_set)
# print(difference1)
difference2 = new_set.difference(old_set)
print(difference2)
for diff in difference2:
	new_dict.pop(diff)
print(new_dict)


