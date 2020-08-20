#PROBLEM
# ask user to i/p a no. containing more than one digit
# example-1256
# calculate 1+2+5+6 and print

#algorithm-(method to solve prob in human language)
# ask i/p in string ex-"1256"
# pick string char one by one and change to int
# int(ex[0])+int(ex[1])...go to len(ex)

num = input("Enter a number containing more than one digit: ")
sum = 0
i = 0
while i < len(num):
    sum+=int(num[i])
    i+=1
print(sum)

