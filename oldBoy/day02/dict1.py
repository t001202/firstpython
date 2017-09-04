
####字典{}  每一个元素就是一个键值对

name = {
	"name":"alex",
	"age":23,
	"gender":"M"
}

print(name["name"])

for info in name: #默认循环输出的key
	print(info)

print(name.get("inf",""))
# print(name.keys())
# print(name.values())
# print(name.items())
# for key,value in name.items():
# 	print(key)
# 	print(value)
