#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

from xml.etree import ElementTree as ET

et_parse = ET.parse("first.xml")
root = et_parse.getroot()
for node in root.iter():
	print(node)
son = root.makeelement('tt',{"name":"123"})
new_s = son.makeelement('tt',{"name":"123"})

son.append(new_s)
root.append(son)
et_parse.write("output.xml")