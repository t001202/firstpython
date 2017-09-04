#元组和列变差不多  列表可以修改 但是元组不可以修改  不可以添加

#如何集合中的元素不可以修改  就使用元组

name_tuple = ("alex","eric")
print(name_tuple)
print(len(name_tuple))
print(name_tuple[0:len(name_tuple)])
for ty in  name_tuple:
	print(ty)

del name_tuple[1]
tuple