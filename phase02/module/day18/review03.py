#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

from xml.etree import ElementTree as ET

ET.register_namespace("url","http://www.caiyi.youyu.com")
root = ET.Element('father',{'name':'19'})
son = ET.Element('son',{'name':'8'})
son.set('text','你好')
root.append(son)
tree = ET.ElementTree(root)
tree.write("family.xml",encoding='utf-8',short_empty_elements=False,xml_declaration=True)
