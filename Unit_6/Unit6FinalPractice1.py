"""
Daniel Villano-Herrera
7/25/2022
Prompting the user the radius of the circle and finding the area and circumference and display the output
"""
pi = 3.14


def area(radius):
    ar = pi * radius**2

    return ar


def circumference(radius):
    cir = 2 * pi * radius
    return cir


rad = int(input("Enter the radius of a circle: "))
print("Here's the area: " + str(area(rad)))
print("Here's the circumference: " + str(circumference(rad)))
