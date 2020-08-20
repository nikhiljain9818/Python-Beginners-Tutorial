# String Formatting


#ask user to input 3 numbers and you have to print average of three
#numbers using string formatting 
#bonus: try to take all three comma separated inputs in one line
num1, num2, num3 = input("Enter three numbers separated by comma: ").split(",")
avg = (int(num1)+int(num2)+int(num3))/3
print(f"Average of three numbers is {avg}")
