## NUMBER GUESSING GAME
## generate a random number
## ask user to guess a no b/w 1 to 100
## if user guess high or low than actual,
## tell him to guess again until he guess correct
## and lastly mention the no of guess attempted



from random import randint
x = randint(1, 101)

num = int(input("Guess a number between 1 to 100: "))
count = 1
while True:
    
    if (num < x):
        print("you guessed too low!")
        num = int(input("guess again: "))
    elif (num > x):
        print("you guessed too high!")
        num = int(input("guess again: "))
    else:
        print(f"you won!!! you took {count} attempts\n !!!GAME OVER!!!")
        break
    count+=1
          
          

          

          
          
          
          

          
          
