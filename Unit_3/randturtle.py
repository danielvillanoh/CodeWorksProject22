"""
Daniel Villano-Herrera
7/13/2022
Create a picture with shapes.
"""

import turtle 
import random

bob = turtle.Turtle()
screen = turtle.Screen()

s = random.randint(0,10)
bob.speed(s)

bob.color("black","white")
screen.screensize(600,600,"lightblue")
bob.begin_fill()
bob.forward(30)
bob.left(30)
bob.forward(30)
bob.left(30)
bob.forward(30)
bob.left(30)
bob.forward(30)
bob.left(30)
bob.forward(30)
bob.left(30)
bob.forward(30)
bob.left(30)
bob.forward(30)
bob.left(30)
bob.forward(30)
bob.left(30)
bob.forward(30)
bob.left(30)
bob.forward(30)
bob.left(30)
bob.forward(30)
bob.left(30)
bob.forward(30)
bob.left(30)
bob.end_fill()

bob.penup()
bob.goto(56,15)
bob.pendown()

ps = random.randint(1,5)
bob.pensize(ps)
bob.color("black","brown")

bob.begin_fill()
bob.right(105)
bob.forward(162)
bob.right(150)
bob.forward(162)
bob.end_fill()

turtle.done()