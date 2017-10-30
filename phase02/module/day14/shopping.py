#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
import pickle

account_file = open("accounts.txt","rb")
# account_file["1000"]["balance"] -= 500
loads = pickle.loads(account_file.read())
loads[1000]["balance"] -= 500
account_file.close()
with open("accounts.txt","wb") as f:
	f.write()
print(loads[1000])
