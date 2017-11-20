#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/16 23:08
__author__ = "WangYx"

from phase03.obj_orient.day20.name_func import get_formatted_name
import unittest
try:
	class NameTestCase(unittest.TestCase):
		def test_firt_name(self):
			formatted_name = get_formatted_name('li','lei')
			self.assertEqual(formatted_name, 'lilei')

	unittest.main()
except:
	print("出异常了")
else:
	print(type(get_formatted_name()))