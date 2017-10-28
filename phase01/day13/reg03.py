#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import re

ret = re.findall(r"^a(\d+)b$", "a23b")
# print(ret)
ret1 = re.findall(r"a(\d+)b","a23414845615b")
ret2 = re.search("a(\d+?)b","a48415615b465165165").group()
ret3 = re.search("(erix)(alex)com\\2","erixalexcomalex").group()
# print(ret3)
ret4 = re.findall("\\babc \\b","abc 454fjafjakl") #r 开头 和相当于将reg规则中的\  转义成\\
# print(ret4)
ret5 = re.search("([0-9]*)([a-z]*)([0-9]*)","123abc456").groups()
print(ret5)
