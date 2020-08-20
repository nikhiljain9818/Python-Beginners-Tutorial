# DUNDER METHODS

class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    # creating dunder methods
    def __add__(self, other):
        return self.salary + other.salary
    def __truediv__(self, other):
        return self.salary / other.salary

    # used to return class onject details
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"
    
    # generally used to display details of the constructor
    def __str__(self):
        return (f"The Name is {self.name}, Salary is {self.salary} and role" 
               f" is {self.role}")
        

emp1 = Employee("Nikhil", 5000, "Programmer")
# emp2 = Employee("Tarun", 1000, "Teacher")
# print(emp1 + emp2)
# print(emp1 / emp2)
print(emp1)
print(repr(emp1))