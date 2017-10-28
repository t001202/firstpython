#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import getpass
username = input("username: ").strip()
password = getpass.getpass("password:")
print(username,password)
