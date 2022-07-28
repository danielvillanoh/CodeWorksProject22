"""
Daniel Villano-Herrera
7/13/2022
Getting a positive number from the user and determine if it's divisible by five random integers from 1 to 10. 
"""
import random
num = int(input("Enter a positive integer: "))

randNum1 = random.randint(1,10)
randNum2 = random.randint(1,10)
randNum3 = random.randint(1,10)
randNum4 = random.randint(1,10)
randNum5 = random.randint(1,10)

if num >= 0:
  if num % randNum1 == 0:
    print(str(num) +" is divisible by " + str(randNum1))
  else:
    print(str(num) + " is not divisible by " + str(randNum1))

  if num % randNum2 == 0:
    print(str(num) +" is divisible by " + str(randNum2))
  else:
    print(str(num) + " is not divisible by " + str(randNum2))
    
  if num % randNum3 == 0:
    print(str(num) +" is divisible by " + str(randNum3))
  else:
    print(str(num) + " is not divisible by " + str(randNum3))
    
  if num % randNum4 == 0:
    print(str(num) +" is divisible by " + str(randNum4))
  else:
    print(str(num) + " is not divisible by " + str(randNum4))

  if num % randNum5 == 0:
    print(str(num) +" is divisible by " + str(randNum5))
  else:
    print(str(num) + " is not divisible by " + str(randNum5))



  
  