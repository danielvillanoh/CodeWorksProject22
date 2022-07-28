"""
Daniel Villano-Herrera
7/13/2022
Generate random values to use in our program.
"""
import random 

radius1 = random.randint(1,100)
radius2 = random.random()
radius3 = random.uniform(1,10)

if radius1 > 50: 
  print("A circle with a radius of " + str(radius1) + " is too large.")
else: 
  area = 3.14 * radius1 ** 2
  print("The area of a circle with a radius " + str(radius1) + " is: " + str(area))

if radius2 < 0.5: 
  print("A circle with a radius of " + str(radius2) + " is too small.")
else: 
  area = 3.14 * radius2 ** 2
  print("The area of a circle with a radius " + str(radius2) + " is: " + str(area))


print("A circle with a radius of " + str(radius3) + " is just right.")
area = 3.14 * radius3 ** 2
print("The area of this circle is: "  + str(area))


