"""
Daniel Villano-Herrera
7/11/2022
Creating a program with user inputs that will ask the user to put information about the vehicle, calculate the mpg, and output it back to the user
"""

vehicle = input("What's the name of your vehicle? ")
color = input("What's the color of your vehicle? ")
miles = float(input("What's the number of miles you have driven since the last time you filled up your tank with gas? "))
gallons = float(input("What's the amount of gas it took to fill up your tank? "))
mpg = miles/gallons

print("Your " + color + " " + vehicle + " got " + mpg + " miles per gallon." )