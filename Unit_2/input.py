"""
Daniel Villano-Herrera
7/11/2022
Getting user input for our program

"""

firstName = input("What is your name? ")

weight = float(input("How much do you weigh? "))
height = float(input("Height in inches: "))

bmi = weight * 703 / height ** 2
print(firstName + ", your BMI is " + str(bmi) + ".")

dogs = int(input("How many dogs do you have? "))
cats = int(input("What about cats? "))
pets = int(input("How many other pets? "))

print("You seem to have " + str(dogs + cats + pets) + " pet(s).")
