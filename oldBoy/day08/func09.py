#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
"""全局变量  :不可以修改  
			  若要修改(全局修改 ,不是局部修改)global
			   全局变量默认都是大写
   局部变量
             默认 都是小写
"""
A = 456   #全局变量
def fun1():
	b  = 123   #局部变量
	print(b)
	print(A)
def fun2():
	global A
	a = 777
	print(a)

fun1()
fun2()



