# common elements finder function
# define a functions which take 2 lists as iputs and return a list
# which contains common elemnets of both lists

list_1 = list(range(1,20))
list_2 = list(range(10,20))

def func(l1,l2):
    list_3 = []
    for i in list_1:
        for j in list_2:
            if i==j:
                list_3.append(j)

    return list_3

print(func(list_1,list_2))


#EXTRA QUES
#find diff b/w max and min munber in the list
##num = [15,561,984,564,51,1889]
##def func(l):
##    return max(num)-min(num)
##print(func(num))

