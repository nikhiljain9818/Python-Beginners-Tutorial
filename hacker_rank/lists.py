n = int(input())
hi = []
for i in range(n):
    c = input().split()
    x = c[0]
    if x == 'append':
        hi.append(int(c[1]))
    if x == "insert":
        hi.insert(int(c[0]),int(c[1]))
    if x == 'remove':
        hi.remove(int(c[1]))
    if x == 'sort':
        hi.sort()
    if x == 'pop':
        hi.pop()
    if x == 'reverse':
        hi.reverse()
    if x == 'print':
        print(hi)
# n = int(input())
# list = []
# for i in range(n):
#     x=input().split()
#     opr=x[0]
#     if opr=="insert":
#         list.insert(int(x[1]),int(x[2]))
#     if opr=="print":
#         print(list)
#     if opr=="remove":
#         list.remove(int(x[1]))
#     if opr=="append":
#         list.append(int(x[1]))
#     if opr=="sort":
#         list.sort()
#     if opr=="pop":
#         list.pop()
#     if opr=="reverse":
#         list.reverse()