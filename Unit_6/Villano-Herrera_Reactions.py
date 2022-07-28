"""
Daniel Villano-Herrera
7/26/2022
This program will react to user input.
"""


def happy():
    print("I love you :D")


def angry():
    print("grrrrr")


def neutral():
    print("uuuuuhhhhhh ... okay.")


q1 = input("Are you a postive person?  ")

if q1.lower() == "yes":
    happy()
elif q1.lower() == "no":
    angry()
else:
    neutral()

q2 = input("Do you love animals? ")

if q2.lower() == "yes":
    happy()
elif q2.lower() == "no":
    angry()
else:
    neutral()

q3 = input("Do you like trains? ")

if q3.lower() == "yes":
    happy()
elif q3.lower() == "no":
    angry()
else:
    neutral()
