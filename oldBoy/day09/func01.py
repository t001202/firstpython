#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import math
def quadratic(a, b, c):
	d = b**2-4*a*c
	x1 = ((-b)+(math.sqrt(d)))/(2*a)
	x2 = ((-b)+(math.sqrt(d)))/(2*a)
	if d < 0:
         print('方程无解 ')
	else:
         print('此方程有两个解：x1=%s,x2=%s'%(x1,x2))

quadratic(1,2,1)