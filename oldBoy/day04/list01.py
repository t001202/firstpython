
li = ["电脑","鼠标垫","U盘","游艇"]

for key,item in enumerate(li):
	print(int(key)+1,item)
inp = input("请输入商品:")  #input无论输入什么格式 都是转成字符串
str = li[int(inp)-1]
print(str)




