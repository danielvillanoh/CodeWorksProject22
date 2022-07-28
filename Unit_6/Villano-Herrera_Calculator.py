"""
Daniel Villano-Herrera
7/25/2022
This program will act as a simple calculator that perform 4 operations.
"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operation = input("Enter a math operation: ")

def addition(number1,number2):
  return number1 + number2

def subtraction(number1,number2):
  return number1 - number2

def multiplication(number1,number2):
  return number1 * number2

def division(number1,number2):
  return number1 / number2

if operation.lower() == "add" or operation.lower() == "addition":
  print(addition(num1,num2))
if operation.lower() == "minus" or operation.lower() == "subtraction":
   print(subtraction(num1,num2))
if operation.lower() == "multiply" or operation.lower() == "multiplication":
   print(multiplication(num1,num2))
if operation.lower() == "divide" or operation.lower() == "division":
   print(division(num1,num2))