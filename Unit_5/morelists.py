"""
Daniel Villano-Herrera
7/20/2022
Exploring list methods
"""
grades = []

values = int(input("Please enter your test score: "))
grades.append(values)

for i in range(5):
  value = int(input("Please enter your test score: "))
  grades.append(value)

print("Here is the list of all your grades: " + str(grades))

result = input("Do you want max or min grade? (Type max or min) ")

if result == "max":
  print("The maximum grade was a: " +       
  str(max(grades)))
elif result == "min":
   print("The minimum grade was a: " +       
   str(min(grades)))
else:
  grades.sort()
  print("Here's the sorted list of grades: " + 
  str(grades))



  