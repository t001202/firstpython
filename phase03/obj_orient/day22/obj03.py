#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017/11/22 22:22
__author__ = "WangYx"

import socketserver as ss

r = ss.ThreadingTCPServer()
r.serve_forever()
