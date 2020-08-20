# String methods

#take two comma separated inputs from user
# 1. user's name
# 2. a single character 

# output - 2 print lines
# 1. user's name length
# 2. count the character that user inputed

#name, char = input("Enter your name and any one character from your name separated by comma: ").split(",")
#print(f"Your name length is: {len(name)}")
#print(f"total no of choosen character in your name is/are: {name.lower().count(char.lower())}")

#ALTERNATE(REMOVE INPUT SPACE)
name, char = input("Enter your name and any one character from your name separated by comma: ").split(",")
print(f"Your name length is: {len(name)}")
print(f"total no of choosen character in your name is/are: {name.strip().lower().count(char.strip().lower())}")


