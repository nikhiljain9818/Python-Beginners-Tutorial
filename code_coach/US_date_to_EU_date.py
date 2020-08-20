# 11/19/2019 or November 19,2019 to 19/11/2019
date =input()
if len(date) <= 10:
    l = list(date.split('/'))
    print(f"{l[1]}/{l[0]}/{l[2]}")
else:
    x = date.split(" ")   #['Jan' , '3,2000']
    y = x[1].split(",")    # ['3' , '2000']
    a = x[0]    # jan
    b = y[0]    # 3
    c = y[1]    # 2000
    if a == "January":
        x = a.replace("January", '1')
    elif a == "February":
        x = a.replace("February", '2')
    elif a == "March":
        x = a.replace("March", '3')
    elif a == "April":
        x = a.replace("April", '4')
    elif a == "May":
        x = a.replace("May", '5')
    elif a == "June":
        x = a.replace("June", '6')
    elif a == "July":
        x = a.replace("July", '7')
    elif a == "August":
        x = a.replace("August", '8')
    elif a == "September":
        x = a.replace("September", '9')
    elif a == "October":
        x = a.replace("October", '10')
    elif a == "November":
        x = a.replace("November", '11')
    elif a == "December":
        x = a.replace("December", '12')
    print(f"{b}/{x}/{c}")
        
    
    



        

