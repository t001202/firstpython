#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import re

origin = "hello alex alex and bcd abc alex"
ret = re.findall(r"a(?:\w+e)x", origin)
print(ret)

# text = "2a3b4c5d6e"
# match = re.match(r"(\d\w\d)+", text)
# print(match.group())
# print(match.groups())
# print(match.groupdict())
