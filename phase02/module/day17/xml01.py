#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

from xml.etree import ElementTree as ET
import requests

root = ET.XML(open("first.xml","r",encoding="utf-8").read())
print(root.tag)

# for node in root:
# 	print(node.tag,node.attrib,node.find("rank").text)

et_parse = ET.parse("first.xml")
root = et_parse.getroot()
for node in root.iter("year"):
	new_year = int(node.text)+1
	node.text = str(new_year)
	node.set("name","alex")
	node.set("age","19")

et_parse.write("output.xml")
