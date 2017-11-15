#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import account as ac

url = input("请输入url: ")

if url.strip().endswith('login'):
	ret = ac.login()
	print(ret)
elif url.strip().endswith('logout'):
	ret = ac.logout()
	print(ret)
else:
	print("404,页面不错在")