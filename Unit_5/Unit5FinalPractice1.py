"""
Daniel Villano-Herrera
7/20/2022
We count and output how many students are in the class and the average grade level of all students. 
"""
levels = [9,10,12,9,9,9,10,11,11,9,10,11,12,9,9,9,10,9,10,9]
print("Here's the total number of students: " + str(len(levels)))

print("Here's how many who are 9th grade: " + str(levels.count(9)))

print("Here's how many who are 10th grade: " + str(levels.count(10)))


print("Here's how many who are 11th grade: " + str(levels.count(11)))


print("Here's how many who are 12th grade: " + str(levels.count(12)))

total = 0 

for numbers in levels: 
  total += numbers

avg = int(total/len(levels))

print("Here's the average grade level in the class: " + str(avg))

      