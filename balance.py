class balance:
	def __init__(self,inter):
		self.interface = inter
		self.x=[]
	def run(self):
		while True:
			a,i = self.interface.getInfo()
			if len(self.x)!=0:
				for num in range(10):
					self.x[num] = a*((1+i)**num)
			else:
				for num in range(10):
					self.x.append(a*((1+i)**num))
			self.interface.showInfo(self.x)