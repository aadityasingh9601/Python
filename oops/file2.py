class Person:
    a = 1
    # A class method is a method which is bound to the class and not the object of the class.
    @classmethod
    def show(self):
        print(f"The instance attribute value of a is {self.a}")

p = Person()
p.a = 33
p.show()

class Employee:
    b = 33
    
    # The method name with ‘@property’ decorator is called getter method. 
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    # Setter method to update the property.
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


empyloyee = Employee()
print(empyloyee.b)
empyloyee.name = "John Doe"
print(empyloyee.fname,empyloyee.lname)


# Operator overloading in Python.
class Number:
    def __init__(self,n):
        self.n = n
    
    # Overloading the functionality of add.
    def __add__(self,num):
        return self.n + num.n
    
    # Multiplication
    def __mul__(self, num):
        return self.n * num.n
    
    # Similarly we can overload other dunder methods functionality too.

a = Number(1)
b = Number(2)

print(a+b)
print(a * b)