class Two_D_vector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        return f"The vector is {self.i}i + {self.j}j"

class Three_D_vector(Two_D_vector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        return f"The vector is {self.i}i + {self.j}j + {self.k}k"

a = Two_D_vector(1,2)
b = Three_D_vector(4,5,6)

print(a.show())
print(b.show())


class Animals:
    def __init__(self,name):
        self.name = name

class Pets(Animals):
    def __init__(self,name,type):
        super().__init__(name)
        self.type = type

class Dog(Pets):
    def __init__(self,name,type):
        super().__init__(name,type)
    
    @staticmethod
    def bark():
        print("Bark!")

dog = Dog("Barky","Domestic")
dog.bark()

class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    # Overload the add & mul method.
    def __add__(self, num):
        return Complex(self.a + num.a, self.b + num.b)
    
    def __mul__(self, num):
        return Complex((self.a * num.a) +  - (self.b * num.b),((self.a * num.b) + (self.b * num.a)))
    
    def __str__(self):
        return f"{self.a} + {self.b}i"
    
c1 = Complex(1,3)
c2 = Complex(4,5)
print(c1+c2)
print(c1 * c2)
