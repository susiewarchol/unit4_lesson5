from turtle import*
import random

turtle= Turtle()

turtle.color("red")
turtle.pensize(5)
turtle.speed(5)
turtle.shape("turtle")

for x in range(3):
	turtle.forward(100)
	turtle.left(120)


mainloop()