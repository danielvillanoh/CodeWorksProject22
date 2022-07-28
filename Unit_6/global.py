"""
Daniel Villano-Herrera
7/25/2022
Using functions and global variables.
"""

import random

count = 0
play_again = True


def generate():
    return random.randint(1, 100)


def prompt():
    global count
    user = int(input("Guess a number from 1-100: "))
    count = count + 1
    return user


def check(n):
    global num
    if n > num:
        print("Your guess is too high")
    else:
        print("Your guess is too low")


def replay():
    global play_again
    global count

    print("You guessed it correctly!")
    print("It took you " + str(count) + " tries.")
    count = 0
    retry = input("Do you want to play again? ")

    if retry.lower() != "yes":
        play_again = False


while play_again:
    num = generate()
    guess = prompt()

    while guess != num:
        check(guess)
        guess = prompt()

    replay()
