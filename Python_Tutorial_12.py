# try/except

""" make a function 'divide(a,b) 
print(divide(4,2)) #2
print(divide(4,0)) #please don't divide by zero
print(divide('4',2)) # type error """
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("please don't divide by zero")
    except ValueError:
        print("Don't type anything other than integer")
    except:
        print("Unexpected Error")
print(divide(num1, num2))
