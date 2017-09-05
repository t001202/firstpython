#有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，
# 将所有大于 66 的值保存至字典的第一个key中，
# 将小于 66 的值保存至第二个key的值中。
#即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}

li = [11,22,33,44,55,66,77,88,99,90]
dirts = {"first":[],"second":[]}
for i in li:
	if i <= 66:
		dirts["first"].append(i)
	else:
		dirts["second"].append(i)

for key,value in dirts.items():
	print(key,len(value))


