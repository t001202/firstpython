msg = "Hello Python i\tam java"
name = "python"
print(msg.capitalize())  #首字母大写
print(msg.upper())    #全部大写
print(name.center(20,"*"))  #字符串居中  使用***填充
print(msg.count("a",0,10))  #查看子序列在字符串中出现的次数  0起始位置  10终止位置  空格也算
print(msg.endswith("va"))  #查看字符串是否以"ph"结尾
print(msg.expandtabs())  #将字符串之间的tab转成空格
print(msg.find("o"))  #在字符串中查找到制定字符出现的第一个位置
print(msg.swapcase())  #大写变小写 小写变大写
