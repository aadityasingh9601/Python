from random import randint

# OBJECT - ORIENTED PROGRAMMING IN PYTHON
# This concept focuses on using reusable code (DRY Principle). 

class Employee:
    # This is a class attribute, each object would have the same value. (Can be changed later after object instantiation)
    company = "Amazon"
    # Class methods are bound to the class itself & not to the object
    @classmethod
    def add(cls,a,b):
        return a + b

    # Method to initialise a object. 
    # "self" is a reference to the current instance of a class.
    def __init__(self,name, salary): # It's a dunder method which is automatically called
        self.name = name
        self.salary = salary

    # Create a method to greet. We've marked as static method to specify that this method doesn't need any information of the
    # object/self parameter.
    @staticmethod
    def greet():
        return "Hello, boss!"
    
    # Create a method to get salary.
    # We also need to accept the argument here using "self"
    def getSalary(self):
        return self.salary
    # Here using "self" is just a convention, because it's descriptive, you can also use something else instead of this.
    # Like any name of your choice. See example below.
    def greet2(random):
        return "Good evening!"
    def getInfo(abc123):
        return f"The company name is {abc123.company}"
    
# Create your object.
firstEmployee = Employee("monster",10000)
print(firstEmployee.add(1,2))
print(firstEmployee.company) 
firstEmployee.company = "Google" # Changing class attribute
firstEmployee.age = "30" # This is an instance attribute
print(firstEmployee.age)
print(firstEmployee.getSalary()) # Internally it converts into firstEmployee.getSalary(firstEmployee)
print(firstEmployee.greet())
print(firstEmployee.greet2())
print(firstEmployee.getInfo())

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


# Inheritance & more on OOPS
# Class Programmer can use the value & attributes of the Employee class.
class Person:
    character = "bad"
    
    @staticmethod
    def whoami():
        return "Animal disguised as a Human"

class Programmer(Employee):
    language = "Java"

progammer = Programmer("harry",20000)

print(progammer.greet())
print(progammer.salary)
print(progammer.company)

class Coder(Employee,Person):
    
    working_hrs = "all day long"

    def __init__(self,name,salary,mental_state):
         # super().__init__() Calls constructor of the base class (Used whenever we want to use contructor of base class)
        super().__init__(name, salary)
        self.mental_state = mental_state

coder = Coder("larry",10000,"ruined")
print(coder.mental_state)
print(coder.character)


class Train:
    seats = 100

    def bookTicket(self,personName):
        self.seats = self.seats - 1;
        return f"Ticket booked for {personName}"
    
    def getStatus(self):
        return self.seats
    
    def getFare(self):
        return f"The fare of train is {randint(200,500)}"


