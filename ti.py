class TextInterface:
	def __init__(self):
		print "Welcome to LC bank!"
		a = 5000
		i = 0.1 
	def getInfo(self):
		a = input("enter a please:")
		i = input("enter i please: ")
		return a,i
	def showInfo(self,r):
		for num in r:
			print num