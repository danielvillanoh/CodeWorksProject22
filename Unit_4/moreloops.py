"""
Daniel Villano-Herrera
7/18/2022
Using loops to validate user input and more 
"""

number = int(input("Please enter an integer between 1 and 100: "))
while number < 1 or number > 100:
  print("Invalid")
  number = int(input("Please enter an integer between 1 and 100: "))

for i in range (1, number + 1):
  if number % i == 0:
    print(str(number) + " is divisible by " + str(i))

