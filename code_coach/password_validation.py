password = input()
spec_char = '!@#$%&*'
num = '1234567890'
a = ''
b = ''
# adding special characters and numbers in a strings
for i in password:
    if i in spec_char:
        a += i
    if i in num:
        b += i
# print(a)
# print(b)
# Validating the condition
if len(a) >= 2 and len(b) >= 2 and len(password) >= 7:
    print('Strong')
else:
    print('Weak')

