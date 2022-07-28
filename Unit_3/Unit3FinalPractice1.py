"""
Daniel Villano-Herrera
7/13/2022
Creating a program that generate a random set of 10 integer grades and calculate and output the average. 
"""

import random
grade1 = random.randint(60,100)
grade2 = random.randint(60,100)
grade3 = random.randint(60,100)
grade4 = random.randint(60,100)
grade5 = random.randint(60,100)
grade6 = random.randint(60,100)
grade7 = random.randint(60,100)
grade8 = random.randint(60,100)
grade9 = random.randint(60,100)
grade10 = random.randint(60,100)

average = (grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7 + grade8 + grade9 + grade10) / 10

print("The average for our 10 integer grades is: " + average)

