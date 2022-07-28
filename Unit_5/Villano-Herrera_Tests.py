"""
Daniel Villano-Herrera
7/20/2022
We will prompt the user to enter test scores and output the average and remove the lowest two scores. 
"""

scores = []

for i in range(10):
  num = int(input("Enter your test score from 0 - 100: "))
  if num > 100 or num < 0: 
    print("That's not a score.")
  else:
    scores.insert(i,num)

scores.remove(min(scores))
scores.remove(min(scores))
total = 0

for num in scores: 
  total += num
avg = total/len(scores)

print("Here's your average grade: " + str(avg))

