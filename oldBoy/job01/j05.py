#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

message = input("请输入字符串: ")
StrCount = 0
NumCount = 0
BlankCount = 0
OtherCount = 0
for i in message:
	if type(i) is int:
		NumCount += 1
	if type(i)	is str:
		StrCount += 1
	if i is " ":
		BlankCount += 1
	else:
		OtherCount += 1
print(StrCount)
print(NumCount)
print(BlankCount)
print(OtherCount)