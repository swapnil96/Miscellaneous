from Tkinter import *
import time
import tkMessageBox
p1 = Tk()
p1.title = "Game 1"
f1 = Frame(p1, height=600, width=600)

def b1call():
	p2 = Tk()
	p2.title('Main')
	w = Canvas(p2, width=600, height=600)
	w.pack()
	r = w.create_rectangle(50, 25, 150, 75, fill="blue")
	a = w.create_line(50, 50, 100, 100)
	while True:
		w.move(r, 0, 5)
		w.move(a, 0, 5)
		w.after(10)
		w.update()
		t = w.coords(r)
		if t[3] == 500:
			break

b1 = Button(p1, text = 'play', command = b1call)
b1.pack(side = BOTTOM)
#b1.place(x =100, y = 200)
f1.pack()

p1.mainloop()
from Tkinter import *
from random import randint

class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")

    def move_ball(self):
        deltax = randint(0,5)
        deltay = randint(0,5)
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(50, self.move_ball)

# initialize root Window and canvas
root = Tk()
root.title("Balls")
root.resizable(False,False)
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

# create two ball objects and animate them
ball1 = Ball(canvas, 10, 10, 30, 30)
ball2 = Ball(canvas, 60, 60, 80, 80)

ball1.move_ball()
ball2.move_ball()

root.mainloop()