"""
Daniel Villano-Herrera
7/26/2022
Creating a "Yahtzee" game
"""
import random

def roll():
  global lis
  lis = []
  
  for i in range(5):
    lis.append(random.randint(1,6))
  print (lis)

def moreOf():
  count = 0 
  num = lis[0]
  for i in lis:
    freq = lis.count(i)
    if freq > count:
      count = freq
      num = i
  print("You should have more of " + str(num) + " to get a Yahtzee.") 

howMany = int(input("How many times would you like to roll? "))


for i in range(howMany):
  roll()
  moreOf()
  