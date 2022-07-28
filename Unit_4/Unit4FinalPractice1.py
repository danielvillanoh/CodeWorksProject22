"""
Daniel Villano-Herrera
7/18/2022
We prompt the user to enter a vowel and if they keep typing something other than a vowel, then we keep prompting them until they finally enter a vowel. 
"""

count = 1 

vowel = input("Enter a vowel: ")

while vowel.lower() != "a" and vowel.lower() != "e" and vowel.lower() != "i" and vowel.lower() != "o" and vowel.lower() != "u":
  print("That is not a vowel")
  vowel = input("Enter a vowel: ")
  count += 1


if count == 1:
  print("You entered a vowel on your first try!")
else:
  print("It took you " + count + " tries to enter a vowel ... sad.")