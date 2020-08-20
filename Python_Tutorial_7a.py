# LISTS

# define a func which will take list containing no. as i/p
# and return list containing square of every elements

numbers = list(range(1,11))

def func(l):
    square_list = []
    for i in numbers:
        square_list.append(i**2)
    return square_list
print(func(numbers))


