#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
import requests
from xml.etree import ElementTree as ET

result_params = requests.get('http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=K234&UserID=')
result_params.encoding="utf-8"
print(result_params.text)
node = ET.XML(result_params.content)
# for n in node.iter("TrainDetailInfo"):



