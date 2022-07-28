"""
Daniel Villano-Herrera
7/20/2022
We will prompt the user a list of 5 names.Based on the input, we will output back the user a list of only the names with even or odd numbers of letters in them. 
"""
names = []

for i in range(5):
  enter = input("Enter a name: ")
  names.insert(i,enter)

oddNames = []
evenNames = []

for name in names: 
  if len(name) % 2 == 0:
    evenNames.append(name)
  else:
    oddNames.append(name)

oddOrEven = input("Do you want to know odd or even names?(Enter odd or even): ")

if oddOrEven.lower() == "even":
  print("Here's the list of even names: " + str(evenNames))
elif oddOrEven.lower() == "odd":
  print("Here's the list of odd names: " + str(oddNames))
else:
  print()
  
userName = input("What's your name?: ")
if userName in names: 
  print("Hey. You have the same name as your friend, " + userName + ".")