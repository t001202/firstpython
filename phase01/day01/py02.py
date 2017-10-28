# coding:utf-8
import getpass

message = input('please enter your name:')
passwd = getpass.getpass('please enter your password:')
if message == 'root' :
	print('enter')
	print(passwd)
else :
	print('sorry')