name = '任'
# for i in name:
# 	#print(i,end='')
# 	bytes_list = bytes(i,encoding='utf-8')
# 	for ns in bytes_list :
# 		print(bin(ns))

print(bytes(name,encoding='gbk'))
print(bytes(name,encoding='utf-8'))
s = 'alex'
print(s[0])
print(len(s))
print(s[0:2])  #  al

start = 0
while start < len(s):
	temp = s[start]
	start += 1
	print(temp,end=" ")


for item in s:
	if item == "l":
		break
	print(item)