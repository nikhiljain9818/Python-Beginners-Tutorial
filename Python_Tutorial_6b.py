num = int(input("Enter the number: "))

def fun(num):
    if (num%2)==0 and (num!=0):
        print("Number is EVEN!")
    elif num==0:
        print("You entered ZERO!")
    else:
        print("Number is ODD!")
fun(num)
