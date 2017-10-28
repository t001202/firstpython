#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
import re

# ret = re.findall("alex.ss","fajfjafalex1sss")
# print(ret)

# ret = re.findall("alex*","fajfjafalexexexxxx1sss")
# print(ret)

# ret = re.findall("alex$","fajfjafalex")
# print(ret)


ret = re.findall("a[bc]s","fajfjafabsexacs1sss")
print(ret)
