from Tkinter import *

def leftKey(event):
    #print "Left key pressed"
   	b = Snake()
   	b.func()



def rightKey(event):
    print "Right key pressed"


class Snake:
	def __init__(self):
		self.p2 = Tk()
		self.frame = Frame(self.p2, width=100, height=100)
		self.p2.title('Main')
		self.w = Canvas(self.p2, width=600, height=600)
		self.w.pack()
		self.frame.pack()
		r = self.w.create_rectangle(50, 25, 150, 75, fill="blue")	
	def move(self):	
		self.p2.bind('<Left>', leftKey)
 		self.p2.bind('<Right>', rightKey)
		self.p2.mainloop()	
	def func(self):
		r = self.w.create_rectangle(30, 25, 150, 75, fill="blue")
		self.p2.mainloop()	

snake = Snake()
snake.move()