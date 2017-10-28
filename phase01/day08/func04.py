#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
"""发邮件"""
def email126():
	import smtplib
	from email.mime.text import MIMEText
	from email.utils import formataddr
	try:
		msg = MIMEText('邮件内容', 'plain', 'utf-8')
		msg['From'] = formataddr(["武沛齐", '17010207437@163.com'])
		msg['To'] = formataddr(["走人", '424662508@qq.com'])
		msg['Subject'] = "主题"

		server = smtplib.SMTP("smtp.126.com", 25)
		server.login("17010207437@163.com", "150832a")
		server.sendmail('17010207437@163.com', ['424662508@qq.com', ], msg.as_string())
		server.quit()
		return "发送成功"
	except:
		return "发送异常: "
def emailqq():
	import smtplib
	from email.mime.text import MIMEText
	from email.utils import formataddr
	try:
		msg = MIMEText('邮件内容', 'plain', 'utf-8')
		msg['From'] = formataddr(["武沛齐", '790479979@qq.com'])
		msg['To'] = formataddr(["走人", '424662508@qq.com'])
		msg['Subject'] = "主题"

		server = smtplib.SMTP("smtp.qq.com", 587)
		server.login("790479979@qq.com", "Wyx1016,.")
		server.sendmail('790479979@qq.com', ['424662508@qq.com', ], msg.as_string())
		server.quit()
		print("发送成功")
	except:
		print("发送异常: ")
# emailqq()
ret = email126()
print(ret)