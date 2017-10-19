#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import urllib.request
url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)
