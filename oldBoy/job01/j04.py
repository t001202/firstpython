# 要求用户输入总资产，例如：2000
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# 附加：可充值、某商品移除购物车
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
total = 2000
flag = True
while flag:
	for key,value in enumerate(goods):
		print(int(key)+1,value)
	index = input("请输入你要购买商品的编号： ")
	if index.isdigit():
		unitPrice = goods[int(index)-1].get("price")
		unitName = goods[int(index)-1].get("name")
		if int(unitPrice)<= total:
			print("您购买的\033[5;31;00m" + unitName + "\033[0m已经加入到购物车中，请您继续购买商品。")
			total -= int(unitPrice)
			print("剩余金额为: "+str(total))
		else:
			print("您购买的\033[5;31;00m" + unitName + "\033[0m 余额不足无法\033[5;31;00m"+unitPrice+"\033[0m 无法继续购买。")



