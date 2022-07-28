"""
Daniel Villano-Herrera
7/20/2022
Loops and Lists in Action
"""

colors = ["red", "orange","yellow", "green","blue"]
answers = []

for c in colors:
  answer = input("Do you like the color - " + c +"? ")
  if answers == "yes":
    print("Me too!")
  answers.append(answer)

totalyes = answers.count("yes")
totalno = answers.count("no")

print("You liked " + str(totalyes) + " colors")
print("You disliked " + str(totalno) + " colors")

newcolor = input("What is another color you like? ")

if newcolor in colors:
  print("I already asked you about that!")
else: 
  print("Thanks for adding that new color to the list.")
  colors.append(newcolor)

total = len(colors)
print("There are " + str(total) + " colors in my list.")

