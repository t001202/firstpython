#列表   进行存放  字符串的集合
li=['li1','li2','li4','li5','li6']
li2=list(['li1','li2','li4','li5','li6',{"key1":"value1","key2":"value2"}])

li.reverse()
li.extend(li2)
print(li)

print(li2[5].get("key2"))
