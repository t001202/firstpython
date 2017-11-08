#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
import pickle
import json

new_dict = {"name":"wangyaxi",
            "age":19,
            "address":"Shanghai",
            "QQ":"575719022",
            "phone":"1370080***",
            "hobby":{
	            "first":"basketball",
	            "second":"football"
                }
            }
dict
# pickle_dumps = pickle.dumps(new_dict)
# print(pickle_dumps)
new_json = json.dumps(new_dict)
print(new_json)
