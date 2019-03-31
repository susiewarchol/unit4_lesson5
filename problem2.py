from turtle import *
import random

turtle = Turtle()

turtle.color("red")
turtle.pensize(5)
turtle.speed(5)
turtle.shape("turtle")

def drawtriangle():
	for x in range(3):
		turtle.forward(100)
		turtle.left(120)

drawtriangle()

for x in range(12):
	drawtriangle()
	turtle.left(30)

mainloop()