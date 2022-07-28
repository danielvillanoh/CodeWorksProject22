"""
Daniel Villano-Herrera
7/13/2022
Creating a turtle graphics program that either draw a square or a triangle based on user input. 
"""
import turtle 

ham = turtle.Turtle()
screen = turtle.Screen()
ham.shape("turtle")

shapePrompt = screen.textinput("Choose Your Shape", "Which shape will you choose? Square or Triangle? ")

turtleSpeed = screen.numinput("Turtle Speed", "Now choose the speed of the turtle. 1 being the slowest, 10 being faster and 0 the fastest. ", 0, 0, 10)

if shapePrompt == "Square" or shapePrompt == "square":
    ham.speed(turtleSpeed)
    ham.left(90)
    ham.forward(100)
    ham.color("black","red")

    ham.begin_fill()
    ham.right(90)
    ham.forward(100)
    ham.right(90)
    ham.forward(100)
    ham.right(90)
    ham.forward(100)
    ham.end_fill()
elif shapePrompt == "Triangle" or shapePrompt == "triangle":
    ham.speed(turtleSpeed)
    ham.forward(100)
    ham.color("black","cyan")

    ham.begin_fill()  
    ham.left(120)
    ham.forward(100)
    ham.left(120)
    ham.forward(100)
    ham.end_fill()
else: 

  


turtle.done()