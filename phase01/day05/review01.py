#coding = utf-8

a = int.__init__(123)

a1 = int(123)
print(a1)

class myInt(object):
	def __init__(self):
		print('init')
	def __call__(self, *args, **kwargs):
		print("okokok")
obj = myInt()



