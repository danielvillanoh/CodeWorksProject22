"""
Daniel Villano-Herrera
7/12/2022
Creating a turtle graphic that will allow the user to "draw" four times. 
"""

import turtle 

bob = turtle.Turtle()
screen = turtle.Screen()

bob.shape("turtle")
moveForward = screen.numinput("Moving Forward","How far should the turtle move forward? Enter from 0-100: ",0,0,100)

bob.forward(moveForward)

changeColor = screen.textinput("Color Change","Now select the color the turtle should change: ")
bob.color(changeColor)

changeAngleDirection = screen.numinput("Direction Change","Now select the angle the turtle should go. Enter from 0-170: ", 0, 0, 170)

bob.left(changeAngleDirection)


moveForward = screen.numinput("Moving Forward","How far should the turtle move forward? Enter from 0-100: ",0, 0,100)

bob.forward(moveForward)

changeColor = screen.textinput("Color Change","Now select the color the turtle should change: ")
bob.color(changeColor)

changeAngleDirection = screen.numinput("Direction Change","Now select the angle the turtle should go. Enter from 0-170: ", 0, 0, 170)

bob.left(changeAngleDirection)


moveForward2 = screen.numinput("Moving Forward","How far should the turtle move forward? Enter from 0-100: ",0, 0,100)

bob.forward(moveForward2)

changeColor2 = screen.textinput("Color Change","Now select the color the turtle should change: ")
bob.color(changeColor2)

changeAngleDirection2 = screen.numinput("Direction Change","Now select the angle the turtle should go. Enter from 0-170: ", 0, 0, 170)

bob.left(changeAngleDirection2)


moveForward3 = screen.numinput("Moving Forward","How far should the turtle move forward? Enter from 0-100: ",0, 0,100)

bob.forward(moveForward3)



turtle.done()