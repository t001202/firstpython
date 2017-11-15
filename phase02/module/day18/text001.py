#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import re
def fetch():
	fetch = []
	flag = "绿灯"
	with open("ha.conf",'r',encoding="utf-8") as file:
		for f in file.readline():
			flag_file = re.findall("backkeng", f)
			if flag_file > 0:
				flag = '红色'

