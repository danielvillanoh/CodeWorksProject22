"""
Daniel Villano-Herrera
7/19/2022
Practice using lists.
"""

names = ["Alice", "Bob","Carl","Dave","Eve"]
print("My friends are: ")
print(names[0])
print(names[1])
print(names[2])

names[0] = "Fran"
del names[1]

print("Now my friends are: ")
print(names[0])
print(names[1])
print(names[2])

if names[3] == "Eve":
  print("I almost forgot to say " + names[3])

