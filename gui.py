from Tkinter import *
class GUInterface:
	def __init__(self):
		self.root = Tk()
		self.root.title("Account Blance")

		self.a = StringVar()
		self.i = StringVar()
		self.a.set('5000.00')
		self.i.set('0.05')
		self.balance = 5000
		self.rate = 0.05

		Label(self.root,text='principle').grid(row=0,column=0,sticky=W)
		Label(self.root,text='interest rate').grid(row=0,column=1,sticky=W)
		self.e1 = Entry(self.root,textvariable=self.a)
		self.e1.grid(row=1,column=0,sticky=W)
		self.e2 = Entry(self.root,textvariable=self.i)
		self.e2.grid(row=1,column=1,sticky=W)
		self.b1 = Button(self.root,text='Submit',command=self.getAmnt)
		self.b1.grid(row=2,column=0,columnspan=2)
		self.c = Canvas(self.root,width=500,height=450,bg='white')
		self.c.grid(row=3,column=0,columnspan=2)
	def getAmnt(self):
		self.balance = eval(self.a.get())
		self.rate = eval(self.i.get())
		self.root.quit()
	def getInfo(self):
		self.root.mainloop()
		return self.balance,self.rate
	def showInfo(self,r):
		self.c.delete('old')
		bottom = 400
		base_x=25
		rect_width = 40
		rect_margin = 7
		maxh =350
		for n in range(10):
			p_x1 = base_x+(rect_width+rect_margin)*n
			p_x2 = p_x1+rect_width
			p_y1 = bottom-r[n]/r[9]*maxh
			num = StringVar()
			year = StringVar()
			year.set('Year %d' % n)
			num.set('%.2f' % r[n])
			self.c.create_text(p_x1,bottom+30,anchor=SW,text='Year %d' % n,tags='old')
			self.c.create_text(p_x1,p_y1-20,anchor=SW,text='%0.2f' % r[n],tags='old')
			self.c.create_rectangle(p_x1,p_y1,p_x2,bottom,tags='old')
	
