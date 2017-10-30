#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
import pickle

dirct = {
	1000: {"name": "alex",
       "email": "lijie162@qq.com",
       "passwd": "123456",
       "balance": 15000,
       "phone": 17010207437,
       "bank_acc": {
	       "ICBC": "4562",
	       "CBC": "1264",
	       "ABC": "9654"
	       }
	},
	1001: {
		"name": "caixin",
	    "email": "SFA162@qq.com",
	    "passwd": "12FG56",
	    "balance": 1000,
	    "phone": 1706955237,
	    "bank_acc": {
		    "ICBC": "45632",
		    "CBC": "16164",
		    "ABC": "963424"
	       }
	},
}
dumps = pickle.dumps(dirct)
with open("accounts.txt","wb") as f:
	f.write(pickle.dumps(dirct))
