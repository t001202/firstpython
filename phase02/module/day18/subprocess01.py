#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"

import subprocess

# ret = subprocess.call("ipconfig")
# print(ret)
# obj = subprocess.Popen(['python'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,
#                  stderr=subprocess.PIPE,universal_newlines=True)
# obj.stdin.write("print(1)\n")
# obj.stdin.write("print(2)\n")
# obj.stdin.close()
obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, universal_newlines=True)
obj.stdin.write("print(1)\n")
obj.stdin.write("print(2)")
# obj.stdin.close()


new_cmd = obj.communicate()
# cmd_out = obj.stdout.read()
# obj.stdout.close()
# cmd_error = obj.stderr.read()
# obj.stderr.close()

print("nw_comd"+str(new_cmd))# print(cmd_out)
# print(cmd_error)

