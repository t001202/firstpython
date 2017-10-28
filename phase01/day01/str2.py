s = "hello {0},age {1}"
print(s)
#{0}  相当于占位符
print(s.format('python',5))  #hello python,age 5
name = "alex"
print(name.index("l"))  #从后往前 返回子序列在字符串中第一次出现的位置 符合find()方法相反
print(name.rindex("l"))
print(name.isalnum())   #判断字符串是否是字符或数字
print(name.isalpha())  #是否是字符
title = "I Hava A Aream"


print(title.istitle())

li = ["alex","eric","py"]
join = "_".join(li)
print(join)

print(title.partition("A"))  #使用A 进行字符串的分隔为 三部分

print(title.replace("Hava","HaVe"))
