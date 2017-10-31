#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
import re

origin = "hello alex and alex is alex who is alex 10"
arithmetic = "1-2*((6-3)*5-6/2+(3+6))+1"
arithmetic1 = "1-2*3+1"
n = origin.split("a")
print(n)
ret = re.split("(a\w+)", origin, maxsplit=1)
print(ret)
n = re.split(r"\(([^(|^)]+)\)", arithmetic1)
print(n)
