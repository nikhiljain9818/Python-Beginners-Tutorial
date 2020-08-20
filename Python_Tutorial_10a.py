# *args

""" input --> num, iterable(tuple, list) containing numbers as args
ex -  num = [1,2,3]
to_power(3,*nums)
output:  list ---> [1, 8, 27]"""

num = [1,2,3]
def to_power(nums, *args):
    if args:
        return [i**nums for i in args]
    
print(to_power(3,*num))

