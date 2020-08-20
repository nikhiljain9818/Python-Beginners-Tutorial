# ask a user for name
# Example-Nikhil Jain
# print count of each word
# output: # N:1.....h:1.... :1.....i:3
          # i:3.....i:3....J:1.....n:1
          # k:1.....l:1....a:1

name = input("Enter your name: ")

i=0                                         
while i < len(name):
    print(f"{name[i]} : {name.count(name[i])}")
    i+=1




