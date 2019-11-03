class A:
	def __init__(self):
		print("A")

	def say(self):
		print("I am A")



class B:
	def __init__(self):
		print("B")

	def say(self):
		print("I am B")



class C(A, B):
	def __init__(self):
		print("c")
		
	def say(self):
		A.say(self)
		B.say(self)


if __name__ == '__main__':
	c = C()
	c.say()