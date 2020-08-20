# Class Method 

class Employee:
    no_of_leaves =8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"Name is (self.name), Salary is (self.salary) and Role is (self.role)"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_string(cls, string):
        params = string.split("-")
        return cls(params[0], params[1], params[2])
        #shortcut
        # cls(*string.split("-"))


nikhil = Employee('Nikhil', 30000, 'Student')
tarun = Employee.from_string("Tarun-70000-Teacher")
print(tarun.salary)
