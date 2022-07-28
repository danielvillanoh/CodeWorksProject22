"""
Daniel Villano-Herrera
7/18/2022
This program will act as a virtual piggy. 
"""

bank = 0 

letter = input("Enter a coin or type DONE when you're finished. \n")

while letter != "DONE": 
  if letter == "Q":
    bank += 25
    letter = input()
  elif letter == "D":
    bank += 10
    letter = input()
  elif letter == "N":
    bank += 5
    letter = input()
  elif letter == "P":
    bank += 1
    letter = input()
  else:
    letter = input("Invalid Coin. Please try again: ")


print("You added $" + str(bank/100) + " to your piggy bank.")