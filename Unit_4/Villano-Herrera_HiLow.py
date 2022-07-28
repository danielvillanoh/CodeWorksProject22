"""
Daniel Villano-Herrera
7/19/2022
Using turtle graphics program to create a high/low guessing game. 
"""

import turtle 
import random

screen = turtle.Screen()
randomNum = random.randint(1,100)

guessNum = screen.numinput("Guess the number", "Try to guess the number between 1 to 100", 0,1,100)

#While the guessing number is not equal to the random number,
while guessNum != randomNum: 

  """
  If the guessing number is bigger than the random number, then the screen background changes to red, we will print out Too High and reprompt the user to guess the number again. 
  """
  if guessNum > randomNum:
    screen.bgcolor("red")
    print("Too High")
    guessNum = screen.numinput("Guess the number", "Try to guess the number again ", 0,1,100)

    """
  If the guessing number is smaller than the random number, then the screen background changes to yellow, we will print out Too Low and reprompt the user to guess the number again. 
  """
  else:
    screen.bgcolor("yellow")
    print("Too Low")
    guessNum = screen.numinput("Guess the number", "Try to guess the number again ", 0,1,100)

"""
The background screen will change to green and print out That's right, if the guessing number is the same as the random number.
"""
screen.bgcolor("green")
print("That's right")