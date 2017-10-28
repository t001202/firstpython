#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import re

text = "i love you, who you love?"
regex = re.compile(r"\d+")

ret = regex.split("one1two2three3four4five")

ret1 = re.search("love",text).span()
equ = "1*2+(2*(3-2))"
ret2 = re.search(r"\([^()]*\)",equ).group()
