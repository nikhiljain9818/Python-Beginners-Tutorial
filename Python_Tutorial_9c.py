# List Comprehension

"""  define a func that take list of strings
list containing reverse of every string
['abc', 'pqr', 'xyz'] -----> ['cba', 'rqp', 'zyx']"""

list_1 = ['Chinese', 'Corona', 'Virus']

def func(l):
   new_list = []
   for i in l:
      new_list.append(i[::-1])
   return new_list
   
print(func(list_1))

""" LIST COMPREHENSION METHOD """

def func(l):
   return [i[::-1] for i in l]
print(func(list_1))
