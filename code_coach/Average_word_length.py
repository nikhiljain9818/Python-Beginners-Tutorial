from math import ceil
input = str(input())
punc = """!@#$%^&*()?"':;<>,./"""
no_punc = ""
for x in input:
    if x not in punc:
        no_punc += x 

word_new = list(no_punc.split())
b = len(word_new)
a = 0
for i in no_punc:
    if (i.isalpha()):
        a+=1
    else:
        pass
print(a)
# print(word_new)
print(ceil(a/b))

