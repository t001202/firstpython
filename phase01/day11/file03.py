#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

with open("ho.log", "r", encoding="utf-8") as f1, open("ho1.log", "w", encoding="utf-8") as f2:
	for line in f1:
		f2.write(line)
