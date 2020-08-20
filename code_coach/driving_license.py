name = str(input())
n = int(input())
hi = list(input().split(" "))
hi.append(name)
new_list = sorted(hi)
# print(new_list)
# print(new_list.index(name))
a = new_list.index(name)


# # if no. of agents are equal or more than the index of my number(my turn number)
# if num_agents >= int(new_list.index(name)):
#     print(20)
# elif num_agents == 1:
#     print((int(new_list.index(name))+1)*20)
# else:
#     if num_agents == 2:
#         if 2 <= new_list.index(name) <= 3:
#             print(40)
#         else:
#             print(60)
#     else:
#         print(40)

if (a+1) <= n:
    print(20)
elif ((a+1) > n) and (a+1 % n == 0):
    print(((a+1)//n)*20)
else:
    print(((a+1//n)+1)*20)