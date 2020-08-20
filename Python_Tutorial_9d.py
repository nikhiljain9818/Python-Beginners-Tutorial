""" define a function to print only numbers to another list as strings
input ---> [True, False, [1,2,3], 1, 1.0, 3]
output ----> ['1', '1.0', '3'] """

list_1 = ['true', 'false', [1,2,3], 1, 1.0, 3]

def func(l):
   list_2 = []
   for i in l:
      if isinstance(i, (int, float)):
         list_2.append(str(i))
   return list_2

print(func(list_1))

""" LIST COMPREHENSION """
##list_2 = [str(i) for i in list_1 if isinstance(i, (int, float))]
##print(list_2)

# or

##list_2 = [str(i) for i in list_1 if type(i) == int or type(i) == float]
##print(list_2)

   
