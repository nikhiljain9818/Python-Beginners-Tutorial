# define a func which will take list as a arg and this func will 
# return a reversed list will return a reversed list

num = list(range(1,11))


def func(l):
    rev_list = []
    for i in num[::-1]:
        rev_list.append(i)
    return rev_list
print(func(num))

# ALTERNATE

##num = list(range(1,11))
##
##def func(l):
##    l.reverse()
##    return l
##
##print(func(num))

    
