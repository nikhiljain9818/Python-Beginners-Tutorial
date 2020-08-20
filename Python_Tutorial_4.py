# and/or Operator

# EXERCISE - WATCH COCO
# Ask user's name and age
# if user's name start with ('a' or 'A') and age is above 10 then
# Print 'you can watch coco movie'
# Else print 'sorry, you cannot watch COCO'

name = input("Enter your name: ")
age = int(input("Enter your age: "))
if (name[0]=="a" or name[0]=="A") and age >= 10:
    print ("you can watch coco movie")
else:
    print("sorry, you cannot watch COCO")


