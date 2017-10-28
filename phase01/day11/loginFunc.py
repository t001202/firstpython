#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"


def login(username, password):
	"""
	函数功能:用于用户名和密码的验证
	:param username: 用户名
	:param password: 密码
	:return: 
	"""
	f = open("ho.log", "r", encoding="utf-8")
	for line in f:
		line = line.strip()
		line_list = line.split("&")
		if username == line_list[0] and password == line_list[1]:
			return True
	return False


def register(username, password):
	"""
	进行用户名注册
	:param username: 
	:param password: 
	:return: 
	"""
	flag = user_exist(username)
	if flag:
		return False
	else:
		with open("ho.log", "a", encoding="utf-8") as f:
			f.write("\n"+username + "&" + password)


def user_exist(username):
	"""
	查询用户名是否存在
	:param username: 
	:return: 
	"""
	f = open("ho.log", "r", encoding="utf-8")
	for line in f:
		line = line.strip()
		line_list = line.split("&")
		if username == line_list[0]:
			return True
	return False


def main():
	print("欢迎登录啪啪啪网站: ", end="\n")
	inp = input("1:登录 ; 2 : 注册 \n")
	if inp == '1':
		user = input("请输入用户名:")
		pwd = input("请输入密码:")
		flag = login(user, pwd)
		if flag:
			print("登录成功")
	elif inp == '2':
		user = input("请输入用户名:")
		userflag = user_exist(user)
		if userflag:
			print("用户名已存在")
		else:
			pwd = input("请输入密码:")
			flag = register(user, pwd)
			if not flag:
				print("注册成功")

