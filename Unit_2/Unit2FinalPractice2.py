"""
Daniel Villano-Herrera
7/11/2022
Creating a turtle graphics program that will allow the user to choose the background color, turtle color, and direction that the turtle is facing and then draw a line. 
"""
import turtle

marie = turtle.Turtle()
screen = turtle.Screen()

marie.shape("turtle")

backgroundColor = screen.textinput("Background Color", "What should be the background color? ")
turtleColor = screen.textinput("Turtle Color", "What should be the turtle color? ")
angle = screen.numinput("Turtle Angle", "What angle should the turtle rotate to the left? Choose between 0 to 90 ", 0 , 90)

screen.bgcolor(backgroundColor)
marie.color(turtleColor)

marie.left(angle)
marie.forward(100)

turtle.done()