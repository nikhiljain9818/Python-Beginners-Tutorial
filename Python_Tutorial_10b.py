""" def a function
names = ['nikhil', 'jain'] ----> ['Nikhil', 'Jain']
print(func(names))
if u call it this way 
print(func(names, reverse_str = True)) ----> ['Lihkin', 'Niaj']"""


name = ['nikhil', 'jain']
def func(*args, reverse_str = False):
    return [i[::-1].title() if reverse_str is True else i.title() for i in args for i in args]
print(func(*name,))

"""name = ['nikhil', 'jain']
def func(*args, reverse_str = True):
    if reverse_str is True:
        return [i[::-1].title() for i in args]
    else:
        return [i.title() for i in args]
print(func(*name,))"""


