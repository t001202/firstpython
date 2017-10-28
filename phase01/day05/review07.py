#元组
t = (11,22,33)
t1 = tuple('123')
t2 = (11,22,["alex",{"key1":"value1","key2":"value3"}])
t3 = t2[2][1]
t3["key3"]="value4"
print(t2)