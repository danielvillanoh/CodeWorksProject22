"""
Daniel Villano-Herrera
7/7/2022
Creating shapes with turtle graphics
"""
import turtle 
bob = turtle.Turtle()
marie = turtle.Turtle()
tyler = turtle.Turtle()

#Creating a triangle
bob.forward(100)
bob.left(120)
bob.color("red")
bob.forward(100)

bob.left(120)
bob.color("green")
bob.forward(100)

#Creating a square

marie.forward(100)
marie.color("white")
marie.forward(100)
marie.color("black")

marie.forward(100)
marie.left(90)
marie.color("red")
marie.forward(100)
marie.left(90)
marie.color("green")
marie.forward(100)
marie.left(90)
marie.color("yellow")
marie.forward(100)


#Creating a hexagon

tyler.forward(300)
tyler.color("white")
tyler.forward(100)
tyler.color("black")

tyler.forward(50)
tyler.left(45)
tyler.color("red")
tyler.forward(50)
tyler.left(45)
tyler.color("green")
tyler.forward(50)
tyler.left(45)
tyler.color("yellow")
tyler.forward(50)
tyler.left(45)
tyler.forward(50)
tyler.left(45)
tyler.color("blue")
tyler.forward(50)
tyler.left(45)
tyler.color("purple")
tyler.forward(50)
tyler.left(45)
tyler.forward(50)


turtle.done()