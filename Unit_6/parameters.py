"""
Daniel Villano-Herrera
7/25/2022
Passing parameters
"""


def grade(number):
    if number >= 90:
        print("You got an A.")
    else:
        print("You didn'\t meet your goal.")


def check(n):
    for char in n:
        if char in "aeiouAEIOU":
            print(char + " is a vowel.")


def compare(num1, num2):
    if num1 > num2:
        return "The first"
    if num1 < num2:
        return "The second"
    if num1 == num2:
        return "Neither"


number1 = float(input("Enter one number: "))
number2 = float(input("Enter another number: "))

score = int(input("What grade did you get on your last test? "))
grade(score)

name = input("What is your name? ")
check(name)

answer = compare(number1, number2)
print(answer + " number is larger.")
