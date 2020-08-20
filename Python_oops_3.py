class Person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instance of {cls.__name__} class"
        
p1 = Person('Nikhil', 'Jain', 20)
p2 = Person('Tarun', 'Jain', 22)
p3 = Person('Arun', 'Jain', 24)

print(Person.count_instances())
print(p2.first_name)
print(p3.age)