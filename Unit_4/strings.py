"""
Daniel Villano-Herrera
7/18/2022
To practice using loops and strings
"""
name = input("Please enter your first and last name: ")
name = name.upper()

reverse = ""

for char in name :
  reverse = char + reverse

print("Your name backwards is " + reverse)

letter = input("What's your favorite letter? ")
letter = letter.upper()

position = name.find(letter)

if position != -1: 
  total = name.count(letter)
  print("Your favorite letter " + letter + " appears " + str(total) + " time/s in your name.")
else:
  print("Your favorite letter " + letter + " doesn\'t appear in your name!")
  