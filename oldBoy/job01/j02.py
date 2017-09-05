#查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。

li = ["alec", " aric", "Alexc", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}

# for i in li:
# 	i.strip()
# 	if i.startswith("a") or i.startswith("A") and i.endswith("c"):
# 		print(i+"  是以a|A 开头以c 结尾的")

for key,value in dic.items():
	v = dic.get(key)
	s = v.strip()
	if (s.startswith("a") or s.startswith("A")) and s.endswith("c"):
		print(s + "  是以a|A 开头以c 结尾的")





