#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
import sys
import time
num = 0
for i in range(21):
	sys.stdout.write("\r")  #清空屏幕
	sys.stdout.write(str(num)+"%  " + "*"*i)
	sys.stdout.flush()
	num += 5
	time.sleep(0.5)
