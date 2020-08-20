# define a func that take list of words as argument and
# return list with reverse of every element in that list
# ['abc','xyz','pqr'] ------> ['cba','zyx','rqp']

num = ['Full','Name','Nikhil','Jain']

def func(l):
    l2 = []
    for i in num:
        l2.append(i[::-1])
    return l2
            
print(func(num))





     

