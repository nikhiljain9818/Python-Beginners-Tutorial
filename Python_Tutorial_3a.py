# if_else

# NUMBER GUESSING GAME
# make a variable,like winning_number and assign any number to it
# if user gussed correctly then print "YOU WIN !!!!"
# if user didn't gussed correctly then:
     # if user gussed lower than actual, then print "too low!"
     # if user gussed higher than actual, then print "too high!"
# google how to generate random number 
from random import randint
x = randint(1, 6)

num=input("Guess a Number between 1 to 10 : ")
num=int(num)
print(f"Random no was {x}")

if num == x:
    print("YOU WIN!!!!")
else:
    if num>x:
        print("too high")
    else:
        print("too low")
        
