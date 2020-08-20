# compute all multiple of 3,5 and add them
# that are less than 100

print(list(range(1, 100)))
sum = 0
for i in range(1, 100):
    if (i%3==0) or (i%5==0):
        sum += i
print(sum)


