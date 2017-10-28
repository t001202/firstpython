
#三大类   运算符   基本数据类型   其他

#运算符  in  判断小字符串是否在大字符串中  类别
        # "lin" in ['lin','h']
#基本上数据类型   :整型 int/number
         #  n = 123  根据int类型 创建一个对象
         # n2 = int(123)

n1 = 12345
n2 = 12345
nleng = n1.bit_length()
n3 = 'hello'
n3leng = n3.__len__()
print(id(nleng))
print(id(n3leng))
print(2**256)