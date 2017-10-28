#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
import re
regex = re.compile(r"\d+")
ret = regex.finditer("12 drump55res flying,12...5...")
m = re.finditer("\d+","12 drump55res flying,12...5...")


retu = re.findall(r"\\","abc\com")

retur = re.findall(r"\babc","adidas abcad")

text = "你好,我是外星人,你在中国听过这个网址吗? www.baidu.com,或者这个网址: www.163.com"
result = re.findall(r"[w]{3}.(?:baidu|163).com",text)
rege = re.compile("[w]{3}.(?:baidu|163).com")
result1 = rege.finditer(text)
for ms in result1:
	print(ms.span(),ms.group())