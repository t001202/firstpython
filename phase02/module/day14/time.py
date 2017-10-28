#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import time
import datetime
# print("start to sleep...")
# time.sleep(5)
# print("end to sleep...")

ctimes = time.ctime(time.time())  #ctime 为时间戳转成时间字符串
time_obj = time.gmtime(time.time())
print(ctimes)
print(time_obj)
print(str(time_obj.tm_year)+"-"+str(time_obj.tm_mon)+"-"+str(time_obj.tm_mday))
print("%d-%d-%d %d:%d" %(time_obj.tm_year,time_obj.tm_mon,time_obj.tm_mday,time_obj.tm_hour,time_obj.tm_min))
print(time.localtime(time.time()-86400))
print(time.strftime("%Y-%M-%d",time.localtime()))
print(time.strptime("2017-10-29","%Y-%m-%d"))