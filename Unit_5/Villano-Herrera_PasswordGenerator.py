"""
Daniel Villano-Herrera
7/20/2022
We will prompt the user for a domain name and the domain name will turn into a password. 
"""

box = []
domain = input("Enter a domain name(facebook,google or amazon): ")

# Adding the strings to the list
if domain == "facebook":
  for letter in domain: 
      box.append(letter)   
elif domain.lower() == "google":
  for letter in domain:
    box.append(letter)
elif domain.lower() == "amazon":
  for letter in domain:
    box.append(letter)
else:
  print()

#We're sorting the list alphabetically 
box.sort()

"""
We're now checking each letter in the list and 
if it's a vowel, then the letter will be 
uppercase
"""
for i in range(len(box)):
    if box[i] == "a" or box[i]  == "e" or box[i]  == "i" or box[i]  == "o" or box[i]  == "u":
     box[i] = box[i].upper()
  
  

#Adding a number to the end, that is the length of #the domain name
box.append(len(domain))

password = ""
#Converting a list into a string
for i in range(len(box)):
  password += str(box[i])

print("Let's convert the domain name into a password: \n "+ domain + " => " + password)