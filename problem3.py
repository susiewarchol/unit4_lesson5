from turtle import *
import random

turtle = Turtle()

turtle.color("red")
turtle.pensize(5)
turtle.speed(5)
turtle.shape("turtle")

for x in range(6):
	turtle.forward(100)
	turtle.left(60)

mainloop()