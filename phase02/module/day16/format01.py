#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

s = "i am %s , my age is %d"%("alex",19)
print(s)
s1 = "i am %(name)s , my age is %(age)d"%{"name":"alex","age":19}
print(s1)
s2 = "i am {} ,age {}".format("alex",18)
print(s2)
s3 = "i am {1},age {0},really {1}".format(18,"alex")
print(s3)