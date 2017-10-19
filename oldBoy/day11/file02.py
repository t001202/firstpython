#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

f = open("ho.log","a",encoding="utf-8")
f.write("789")
f.flush()
print(f.tell())