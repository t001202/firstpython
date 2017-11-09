#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

from xml.etree import ElementTree as ET

ET.parse()
root = ET.Element('mounth',{'name':'2016'})
son = ET.Element('years',{'name':'2013'})
root.append(son)