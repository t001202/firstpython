#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

f = open("hello.log", "w")
str = "中国人"
new_str = bytes(str,encoding="utf-8");
f.write(str)
f.close()
