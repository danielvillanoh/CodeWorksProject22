"""
Daniel Villano-Herrera
7/18/2022
Creating a turtle grpahics program that will draw a circle that gradually increases in size, however many times the user specifies.
"""

import turtle 

bob = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("red")
bob.color("cyan")
bob.shape("turtle")

num = screen.numinput("Enter a number." , "Enter a number between 1 and 20: ",0,1,20)


for i in range(int(num)):
  bob.begin_fill()
  bob.circle(i * num)
  bob.end_fill()


turtle.done()