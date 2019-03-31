from turtle import *
import random

turtle = Turtle()

turtle.color("red")
turtle.pensize(5)
turtle.speed(0)
turtle.shape("turtle")

def drawhexagon():
	for x in range(6):
		turtle.forward(100)
		turtle.left(60)

		for x in range(25,150,25):
			drawhexagon()

mainloop()