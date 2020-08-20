# Overiding

class A:
    classvar = "I am a class variable  in class A"
    def __init__(self):
        self.var1 = "I an inside class A constructor"
        self.classvar = "I am a instant variable in class A"
        self.special = "I am special"

class B(A):
    classvar = "I am a class variable  in class B"
    def __init__(self):
        # Now there is no existence of class A contructor since we override it here
        self.var2 = "I an inside class B constructor"
        self.classvar = "I am a instant variable in class B"

obj1 = A()
obj2 = B()
# print(obj2.special)
# print(obj2.var1)


# Super Method
class C:
    classvar = "I am a class variable  in class C"
    def __init__(self):
        self.var3 = "I an inside class C constructor"
        self.classvar = "I am a instant variable in class C"
        self.special = "I am special"

class D(C):
    classvar = "I am a class variable  in class D"
    def __init__(self):
        super().__init__()
        self.var4 = "I an inside class D constructor"
        self.classvar = "I am a instant variable in class D"

c = C()
d = D()
print(d.special)
print(d.var3)
