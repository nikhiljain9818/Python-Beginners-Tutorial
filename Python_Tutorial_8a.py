# Dictionary

# define a func that takes a number (n)
# return a dict containing cube of numbers from 1 to n
# ex ----> {1:1, 2:8, 3:27}

n = int(input("Enter number: "))

def func(n):
    count = {}
    i = 1
    while i < n+1:
        count[i]= i**3
        i += 1
    return count

print(func(n))
