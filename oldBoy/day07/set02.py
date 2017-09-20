#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

#set 的方法功能 add clear difference difference_update
se = set([11,22,33,44])
be = set([11,22])
de = se.difference(be)
print(de)
#me = se.difference_update(be)
print(se)
se.remove(11)
print(se)
se.discard(55)
print(se)
