"""
Daniel Villano-Herrera
7/13/2022
Creating a 4 question quiz and inform whether they got the question right. 
"""


score = 0

print("Answer the questions by typing in true or false.")
question1 = input("Is every animal with a tail is a dog? ")
question2 = input("Is 10 is divisible by 2? ")
question3 = input("Is the sun blue? ")
question4 = input("Is there a bacon in the bacon, egg, and cheese sandwich? ")

if question1 == "False" or question1 == "false":
  print("That's correct!")
  score += 25
elif question1 == "True" or question1 == "true": 
  print("That's incorrect.")
  
else: 
  print("Not an answer.")

if question2 == "True" or question2 == "true":
  print("That's correct!")
  score += 25
elif question2 == "False" or question2 == "false": 
  print("That's incorrect.")
else: 
  print("Not an answer.")

if question3 == "False" or question3 == "false":
  print("That's correct!")
  score += 25 
elif question3 == "True" or question3 == "true": 
  print("That's incorrect.")
else: 
  print("Not an answer.")

if question4 == "True" or question4 == "true":
  print("That's correct!")
  score += 25
elif question4 == "False" or question4 == "false": 
  print("That's incorrect.")
else: 
  print("Not an answer.")

print("Here your total score: " + str(score) +"%")