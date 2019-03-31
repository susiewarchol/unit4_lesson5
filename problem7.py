from turtle import *
import random

turtle = Turtle()
turtle.color("red")
turtle.pensize("5")
turtle.speed(5)
turtle.shape("turtle")

def drawstar():
	for x in range(5):
		turtle.forward(150)
		turtle.left(144)

def row():
	for x in range(3):
		drawstar()
		turtle.penup()
		turtle.forward(60)
		turtle.pendown()

for x in range(5):
	row()
	drawstar()
	turtle.penup()
	turtle.right(90)
	turtle.backward(300)
	row()

mainloop()