with open('file1.txt', 'r') as f1:
    with open('file2.txt', 'w') as f2:
        for line in f1.readlines():
            name, salary = line.split(',')
            f2.write(f"{name} salary is {salary}")


    
    