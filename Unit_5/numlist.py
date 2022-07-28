"""
Daniel Villano-Herrera
7/20/2022
Lists with numbers
"""
numbers = [10,25,40,55,70,85,100]
begtotal = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5] + numbers[6]

print("The total of all numbers is: " + str(begtotal))
n = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

numbers[0] = n
numbers[6] = n2

newtotal =numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5] + numbers[6]

print("The new total of all numbers is: " + str(newtotal))

