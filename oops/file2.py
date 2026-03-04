class Person:
    a = 1
    # A class method is a method which is bound to the class and not the object of the class.
    @classmethod
    def show(self):
        print(f"The instance attribute value of a is {self.a}")

p = Person()
p.a = 33
p.show()