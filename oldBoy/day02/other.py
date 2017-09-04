# li = ["电脑","手机","音响"]
# for key,value in enumerate(li,1):
# 	print(key,value)
# imp = input("请输入商品:  ")
# imp = int(imp)
# print(li[imp-1])

#range xrange
# for temp in range(100):
# 	print(temp)
# #py3版本中没有了xrange  使用xrange替代了两个
# for tt in range(10,1,-1):
# 	print(tt)

li = ["alex","tony"]
le = len(li)
for str in range(0,le):
	print(str,li[str])