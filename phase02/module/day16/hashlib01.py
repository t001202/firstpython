#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
import hashlib

# hash = hashlib.md5()
# hash.update(bytes('123',encoding="utf-8"))
# print(hash.hexdigest())
import sys
import os
ret = os.environ
for i in ret.items():
	print(i[0],i[1])