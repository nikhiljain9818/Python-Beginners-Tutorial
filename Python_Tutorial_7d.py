# FILTER ODD-EVEN
# define a func and input list---->[1,2,3,4,5]
# output ----> [[1,2,5,7], [2,4,6]]

num = list(range(1,11))

def func(l):
    even = [[],[]]
    for i in num:
        if i%2==0:
            even[0].append(i)
            
        else:
            even[1].append(i)
    return even
            
    

print(func(num))
            
