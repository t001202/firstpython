#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import configparser

con = configparser.ConfigParser()
con.read("ini",encoding="gbk")
ret = con.sections()
con.set("wyx","address","河南")
con.add_section("wy")
con.set("wy","age","18")
flag = con.has_section("wyl")
print(flag)
has_option = con.has_option("wyl", "agee")
print(has_option)
con.write(open("ini","r+"))
