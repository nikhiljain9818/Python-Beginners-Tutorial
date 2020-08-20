# wap to tell no. of list inside a list
# ex- input-->[1,2,3, [1,2], [3,4]]  output---> 2

num = [1,2,3, [1,2], [3,4],]

def func(l):
    count = 0
    for i in num:
        if type(i) == list:
            count += 1
    return count

print(func(num))



    


