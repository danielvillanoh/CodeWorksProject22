"""
Daniel Villano-Herrera
7/11/2022
Controlling our turtle with user input
"""

import turtle
bob = turtle.Turtle()


screen = turtle.Screen()
screen.bgcolor("yellow")


bob.shape("turtle")

num = screen.numinput("Forward movement,", "How much should the turtle move?")
bob.forward(num)

angle = screen.numinput("Rotate Left", "How much should the turtle rotate?", 90, 0, 360)
bob.left(angle)

color = screen.textinput("Color","Please enter a common color.")
bob.color(color)

turtle.done()