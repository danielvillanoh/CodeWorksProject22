"""
Daniel Villano-Herrera
7/20/2022
Creating a program that will allow the user to enter specific number of names. After getting all the names the user wanted to enter, we remove all duplicate names in the list and then output unique names on the list. 
"""
list = []

name = input("Enter a name: ")

duplicates = int(input("Enter how many times: "))

for i in duplicates:
  list.append(name)

print(list)
