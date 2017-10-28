###列表  元素的集合  相当于java中的数组####
name = "任慧阳"
nl= ["alex",name,"tony"]
nl.append("wyx")
nl.append("wyx")
nl.append("wyx")
print(nl)
temp = [111,222,333]
print(nl.count("wyx"))
nl.extend(temp)
print(nl)
nl.insert(1,"sb")
print(nl)