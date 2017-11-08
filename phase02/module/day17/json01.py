#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
import urllib.request
import requests
url_path = 'http://wthrcdn.etouch.cn/weather_mini?city=上海'
result_3 = requests.request('get','http://www.baidu.com')
print(result_3)

# req = urllib.request.Request(url_path)
# ret = urllib.request.urlopen(req)
# result = str(ret.read(),encoding="utf-8")
# print(result)

# ret = request.urlopen('http://wthrcdn.etouch.cn/weather_mini?city=%E5%8C%97%E4%BA%AC')
# print(str(ret,encoding="utf-8"))
# weather_str = {"data": {
# 	"yesterday": {"date": "6鏃ユ槦鏈熶竴", "high": "楂樻俯 22鈩�", "fx": "涓滃崡椋�", "low": "浣庢俯 16鈩�", "fl": "<![CDATA[<3绾]>",
# 	              "type": "澶氫簯"}, "city": "涓婃捣", "aqi": "177", "forecast": [
# 		{"date": "7鏃ユ槦鏈熶簩", "high": "楂樻俯 21鈩�", "fengli": "<![CDATA[<3绾]>", "low": "浣庢俯 15鈩�", "fengxiang": "瑗块",
# 		 "type": "闃�"}, {"date": "8鏃ユ槦鏈熶笁", "high": "楂樻俯 22鈩�", "fengli": "<![CDATA[4-5绾]>", "low": "浣庢俯 13鈩�",
# 		                 "fengxiang": "鏃犳寔缁鍚�", "type": "澶氫簯"},
# 		{"date": "9鏃ユ槦鏈熷洓", "high": "楂樻俯 20鈩�", "fengli": "<![CDATA[3-4绾]>", "low": "浣庢俯 14鈩�", "fengxiang": "涓滈",
# 		 "type": "澶氫簯"},
# 		{"date": "10鏃ユ槦鏈熶簲", "high": "楂樻俯 20鈩�", "fengli": "<![CDATA[4-5绾]>", "low": "浣庢俯 11鈩�", "fengxiang": "涓滈",
# 		 "type": "闃�"},
# 		{"date": "11鏃ユ槦鏈熷叚", "high": "楂樻俯 15鈩�", "fengli": "<![CDATA[<3绾]>", "low": "浣庢俯 11鈩�", "fengxiang": "涓滃寳椋�",
# 		 "type": "澶氫簯"}], "ganmao": "澶╁喎椋庡ぇ锛屾槗鍙戠敓鎰熷啋锛岃娉ㄦ剰閫傚綋澧炲姞琛ｆ湇锛屽姞寮鸿嚜鎴戦槻鎶ら伩鍏嶆劅鍐掋€�", "wendu": "18"}, "status": 1000,
#                "desc": "OK"}
# import json
#
#
# json_dumps = json.dumps(weather_str)
# json_loads = json.loads(json_dumps)
# for key in json_loads.keys():
# 	value = json_loads[key]
#
# 	print(str(value))

