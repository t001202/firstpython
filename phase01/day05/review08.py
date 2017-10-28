#字典

a = {"k1":"v1","k2":"v2"}
a2 = dict(k1=123,k2=234)

a3 = dict.fromkeys(["k1","k2","k3"],[])
print(a3)
a3["k1"] = "alex"
print(a3)