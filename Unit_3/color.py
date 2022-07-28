"""
Daniel Villano-Herrera
7/12/2022
Using the elif for favorite colors. 
"""
color = input("What is your favorite color? ")

if color == "pink" or color == "red":
  print("That's my favorite color.")
elif color == "brown" or color == "grey" or color == "white":
  print("That is so not right.")
else: 
  print("That's an okay color.")

if color == "purple":
  print("That's my sister's favorite color.")

if color != "orange" and color != "blue":
  print("Where's the school spirit?")
else:
  print("You have school spirit!")
