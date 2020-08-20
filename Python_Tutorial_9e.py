""" wap to create a new list from old list that contain odd num as negative
odd and even numbers as twice of old
[1, 2, 3, 4, 5, 6] ----> [-1, 4, -3, 8, -5, 12]"""

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(l):
    list_2 = []
    for i in l:
        if i%2 != 0:
            list_2.append(-i)
        else:
            list_2.append(i*2)
    return list_2

print(func(list_1))

""" LIST COMPREHENSION METHOD """
##list_2 = [-i if (i%2 != 0) else i*2 for i in list_1]
##print(list_2)


        
