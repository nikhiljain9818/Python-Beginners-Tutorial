# elif-else

# show ticket pricing
# 1 to 3 - free
# 4 to 10 - 100
# 11 to 50 - 250
# above 50 - 150

print("Welcome to UNITY MALL\n Apka bohot-bohot swagar hai ")
age = int(input("Please,Enter your AGE: "))
if 0<age<=3:
    print("Your Ticket is free,ENJOY!!!")
elif 4<age<=10:
    print("Your Ticket price is 100,ENJOY!!!")
elif 11<age<=50:
    print("Your Ticket price is 250,ENJOY!!!")
else:
    print("Your Ticket price is 150,ENJOY!!!")

