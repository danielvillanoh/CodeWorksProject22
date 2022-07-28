"""
Daniel Villano-Herrera
7/26/2022
Testing randomness of lists.
"""


import random 

my_list = ["game1", "game2","game3"]

num = random.randint(0,2)

print("Here's the game you should play: " + my_list[num])