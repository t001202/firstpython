#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
import requests
from xml.etree import ElementTree as ET
requests_get = requests.get("http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=575719022")
requests_get.encoding="utf-8"
node = ET.XML(requests_get.content)
if node.text == "Y":
	print("在线")
else:
	print("离线")

