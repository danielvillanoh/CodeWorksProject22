"""
Daniel Villano-Herrera
7/19/2022
Creating a program that will take a sentence entered by a user and count how many letters in your first name are in a sentence. 
"""

sentence = input("Please enter a sentence: ")
name = "Daniel"
letterFound = ""
count = 0
for letter in sentence:
  if letter == "D" or letter == "d" or letter == "A " or letter == "a" or letter == "N" or letter == "n" or letter == "I" or letter == "i" or letter == "E" or letter == "e" or letter == "L" or letter == "l":
    letterFound += letter
    count += 1 

count = len(letterFound)
print(letterFound)
print("There were " + str(count) + " that shared the letters of my name " + name+ ".")