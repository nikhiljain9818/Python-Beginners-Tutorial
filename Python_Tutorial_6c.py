# def a func which takes two no as i/p and return greater of two no.

x, y = input("Enter two numbers separated by comma: ").split(",")

def is_greater(x,y):                  #ALTERNATE
    if(x>y):                          #def is_greater(x,y):
        return x                          #print(max(x,y))
    return y   
print(is_greater(x,y))                #print(is_greater(x,y))

# def a func which takes three no as i/p and return greater of three no.

x, y, z = input("Enter three numbers separated by comma: ").split(",")

def is_greatest(x,y,z):
    if (x>y) and (x>z):
        print(f"{x} is greatest among {x},{y},{z}")
    elif (y>z) and (y>x):
        print(f"{y} is greatest among {x},{y},{z}")
    else:
        print(f"{z} is greatest among {x},{y},{z}")
is_greatest(x,y,z)

#SHORTCUT
x, y, z = input("Enter three numbers separated by comma: ").split(",")

def is_greatest(x,y,z):
    print(max(x,y,z))
is_greatest(x,y,z)

     
