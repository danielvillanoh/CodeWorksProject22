"""
Daniel Villano-Herrera
7/18/2022
Creating basic loops in our program
"""

guess = 1 
age = int(input("How old do you think I am? "))

while age != 30:
  age  = int(input("How old do you think I am? "))
  guess = guess + 1

print("You finally guessed it, it took you " + str(guess) + " tries.")

answer = input("What do you think my favorite color is? ")
for i in range(3):
  if answer == "Orange": 
    print("You are right!")
  else:
    print("WRONG")
