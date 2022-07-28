"""
Daniel Villano-Herrera
7/25/2022
Creating functions
"""


def name():
    n = input("Please enter your name: ")
    print("I have two questions for you " + n + ".")


def question1():
    answer1 = input("Do you like cheese? ")
    if answer1.lower() == "yes":
        print("Swiss is my favorite.")


def question2():
    answer2 = int(input("How many inches tall are you? "))
    if answer2 > 67:
        print("You're taller than me.")


print("Welcome to my program")
name()
question1()
question2()
print("Thanks for running the program.")
