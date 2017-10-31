#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import re

origin = "hello alex and i am alexj ,who is he do you know alex ? what"
sub = re.sub("alex\w*", "kkk", origin)
new_sub, count = re.subn("alex\w*", "KKK", origin)
print(sub)
print(new_sub, " \n个数: "+str(count))
