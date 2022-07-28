"""
Daniel Villano-Herrera
7/26/2022
Creating a "Yahtzee" game
"""
import random

"""
Creating a roll function where we make a list of 5 random numbers and we print out these numbers.
"""
def roll():
  global lis
  lis = []
  
  for i in range(5):
    lis.append(random.randint(1,6))
  print (lis)


howMany = int(input("How many times would like to roll? "))

"""
This function will compare the previous count and the current count of element to see which one is more frequent. 
"""
def moreOf():
  count = 0 
  num = lis[0]
  for i in lis:
    freq = lis.count(i)
    if freq > count:
      count = freq
      num = i
  print("You should have more of " + str(num) + " to get a Yahtzee.") 

  
for i in range(howMany):
  roll()
  
  
