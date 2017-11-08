#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import os
from phase02.module.day17 import review01

# print(review01.__author__)
# print(review01.__name__)
# print(__file__)
# dirPath = os.path.dirname(__file__)
# print(dirPath)

current_filepath = __file__
dirname = os.path.dirname(current_filepath)
os_path_join = os.path.join(dirname,"bin")
print(os_path_join)
