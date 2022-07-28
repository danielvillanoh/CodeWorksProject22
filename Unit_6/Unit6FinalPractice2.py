"""
Daniel Villano-Herrera 
7/25/2022
This program will prompt the user for a word. Based on the length of the word, one of three scenario happens. 
"""
global worde
worde = input("Enter a word: ")
wordLength = len(worde)


def consonants():
    global vowel
    global con
    con = ""
    vowel = "aeiouAEIOU"
    for letter in worde:
        if letter not in vowel:
            con += letter
    return con


def backwards():
    global backward
    backward = ""
    for letter in worde:
        backward = letter + backward

    return backward


def otherLetter():
    global lst
    lst = []
    global words
    words = ""
    for i in range(len(worde)):
        lst.append(worde[i])

    for i in range(len(lst)):
        words += str(lst[i])

    return words


if wordLength < 5:
    print(consonants())

elif wordLength >= 5 and wordLength <= 9:
    print(backwards())

else:
    print(otherLetter())