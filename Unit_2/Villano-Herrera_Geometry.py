"""
Daniel Villano-Herrera
7/12/2022

Calculating the volume of a sphere, pyramid and cylinder based on the input from the user.
"""


radius = float(input("Enter any radius: "))

length = float(input("Enter any length: "))

width = float(input("Enter any width: "))

height = float(input("Enter any height: "))

pi = 3.14
volSphere = 4/3 * pi * radius ** 3
volPyramid = (length * width * height)/3
volCylinder = pi * radius**2 * height

print("Here are the volumes of a sphere, pyramid, and cylinder based on your input: \nVolume of a Sphere: " + str(volSphere) + "\nVolume of a Pyramid: " +  str(volPyramid) + " \nVolume of a Cylinder: " + str(volCylinder))

