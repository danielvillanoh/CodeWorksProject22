"""
Daniel Villano-Herrera
7/13/2022
Drawing a bottle by using turtle graphics.
"""
import turtle
nolan = turtle.Turtle()

nolan.color("black","orange")

nolan.begin_fill()
nolan.forward(100)
nolan.left(90)
nolan.forward(200)
nolan.left(90)
nolan.forward(100)
nolan.left(90)
nolan.forward(200)
nolan.end_fill()

nolan.penup()
nolan.left(180)
nolan.forward(150)
nolan.pendown()

#White Rectangle on the middle
nolan.right(90)
nolan.color("black","white")
nolan.begin_fill()
nolan.forward(100)
nolan.right(90)
nolan.forward(60)
nolan.right(90)
nolan.forward(100)
nolan.end_fill()

nolan.right(90)
nolan.forward(60)

nolan.right(90)
nolan.forward(40)

#Moving to the middle of the white rectangle
nolan.penup()
nolan.right(90)
nolan.forward(15)
nolan.pendown()

nolan.color("black","blue")

#Making the F letter. 
nolan.begin_fill()
nolan.forward(40)
nolan.left(90)
nolan.forward(10)
nolan.left(90)
nolan.forward(15)
nolan.right(90)
nolan.forward(15)
nolan.left(90)
nolan.forward(10)
nolan.left(90)
nolan.forward(15)
nolan.right(90)
nolan.forward(10)
nolan.right(90)
nolan.forward(15)
nolan.left(90)
nolan.forward(10)
nolan.left(90)
nolan.forward(25)
nolan.end_fill()

nolan.left(90)
nolan.forward(10)

nolan.penup()
nolan.left(180)
nolan.forward(70)
nolan.pendown()

nolan.left(90)
nolan.forward(40)
nolan.right(90)
nolan.color("black","grey")

#Upper part of the bottle
nolan.begin_fill()
nolan.goto(40,250)
nolan.right(90)
nolan.forward(25)
nolan.goto(100,200)
nolan.end_fill()

#Creating the bottle cap
nolan.penup()
nolan.goto(40,250)
nolan.pendown
nolan.color("black","green")

nolan.right(180)

nolan.begin_fill()
nolan.forward(10)
nolan.right(90)
nolan.forward(20)
nolan.right(90)
nolan.forward(45)
nolan.right(90)
nolan.forward(20)
nolan.right(90)
nolan.forward(10)
nolan.end_fill()


turtle.done()