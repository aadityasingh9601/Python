# OBJECT - ORIENTED PROGRAMMING IN PYTHON
# This concept focuses on using reusable code (DRY Principle). 

class Employee:
    company = "Amazon" # Each object would have the same value.

    # Class methods are bound to the class itself & not to the object
    @classmethod
    def add(cls,a,b):
        return a + b

    # Method to initialise a object. It's the contructor function.
    # "self" is a reference to the current instance of a class.
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

    # Create a method to greet.
    @staticmethod
    def greet():
        return "Hello, boss!"
    
    # Create a method to get salary.
    def getSalary(self):
        return self.salary
    
# Create your object.
firstEmployee = Employee("monster",10000)
print(firstEmployee.add(1,2))

print(firstEmployee.company)
firstEmployee.company = "Google"
print(firstEmployee.company)
print(firstEmployee.name)
print(firstEmployee.getSalary())
print(firstEmployee.greet())

class Calculator:
    @staticmethod
    def greet():
        print("Hello, user")

    def square(self,n):
        return n * n
    
    def cube(self,n):
        return n * n * n
    
mycalc = Calculator()
mycalc.greet()
print(mycalc.square(14))
print(mycalc.cube(17))

class Person:
    character = "bad"

    def whoami(self):
        return "Animal disguised as a Human"


# Inheritance & more on OOPS
# Class Programmer can use the value & attributes of the Employee class.
class Programmer(Employee):
    language = "Java"

progammer = Programmer("harry",20000)

print(progammer.greet())
print(progammer.salary)
print(progammer.company)

class Coder(Employee,Person):
    
    working_hrs = "all day long"

    def __init__(self,name,salary,mental_state):
         # super().__init__() Calls constructor of the base class 
        super().__init__(name, salary)
        self.mental_state = mental_state

coder = Coder("larry",10000,"ruined")
print(coder.mental_state)
print(coder.character)
