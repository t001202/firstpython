#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

#open("文件名","模式(只读,只写,读写,追加)","编码")
f = open('love.log',encoding='utf-8')
data = f.read()
f.close()
print(data)
