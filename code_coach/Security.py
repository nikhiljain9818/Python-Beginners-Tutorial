string ='xxxGGTxxxxxxM'
hlo = string.split('G')
print(hlo)
a = True
for i in hlo:
    if 'T' in i and 'M' in i:
        a = False
        print("Alarm")
        break
        
if a:
    print('quiet')


# if '$' and 'T' and 'G' in string:



# hi = 'xxxxxTGGGxxxMxxxG'
# hlo = hi.split('G')
# print(len(hlo))
# print(hlo)
# a = True
# for i in hlo:
#     if (i.index('T') > 0) and (i.index('M') > 0):
#         a = False
#         print("Alarm")
#         break
# if a:
#     print("OK")

    