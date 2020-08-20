# Multiple Inheritence

class Employee:
    no_of_leave = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}, salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leave = newleaves
    
class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game
    
    def printdetails(self):
        return f'The Name is {self.name} and game is {self.game}'

class CoolProgrammer(Player, Employee):
    language = "C++"
    def printlanguage(self):
        print(self.language)

nikhil = Employee("Nikhil", 40000, "Instructor")
tarun = Employee("Tarun", 80000, "Student")        

vishal = CoolProgrammer("Vishal", "Cricket")
det = vishal.printdetails()
print(vishal.printlanguage())
print(det)           



        