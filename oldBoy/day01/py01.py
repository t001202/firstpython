import getpass

message = input("请输入用户名: ")
paswd = getpass.getpass("请输入密码: ")
count = 3
if message == "admin":
	print("您是超级管理员,可以进行下一步")
	# while True:
	# 	if paswd == '123456':
	# 		print("密码正确,请进入!!!")
	# 	else:
	# 		print("密码错误!!!")
	# 		count = int(count) -1
	# 		if int(count) >= 0:
	# 			print("你还可以输入"+count+"机会")
	# 		else:
	# 			break
else:
	print("对不起,您的权限不够,不能进行下一步操作.")