#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import logging

log_file1 = logging.FileHandler("log1.log",'a',encoding='utf-8') #追加
fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
log_file1.setFormatter(fmt=fmt)

log_file2 = logging.FileHandler("log2.log",'w',encoding='utf-8')#  重新写进去
fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
log_file2.setFormatter(fmt=fmt)

logger = logging.Logger("s1",level=logging.ERROR)
# logger2 = logging.Logger("s2",level=logging.INFO)
logger.addHandler(log_file1)
logger.addHandler(log_file2)


logger.critical("hello python this is the first log and it is log.log")
