"""the user enters a string and a substring. You have to print the number of times that the 
substring occurs in the given string."""

line = input()
char = input()
count = 0
for i in range(len(line)):
    if line[i:i+len(char)] == char:
        count += 1
    else:
        pass
print(count)



