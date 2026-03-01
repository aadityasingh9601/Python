# Functions & Recursion

# Some in-built functions.
# len(), print(), range() 

# User defined functions.

def first():
    print("Hello everyone!")

print("Calling function 10 times ---")
for i in range (1,11):
    first()

def greet(user = "test user"):
    print("Good evening!", user)

username = input("Enter your username --> ")
greet(username)

# Recursion

def findFactorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * findFactorial(n-1)
    
print(findFactorial(10))

# Find greatest of three numbers

def findGreatest(a,b,c):
    greatest = 0
    if a > greatest:
        greatest = a
    if b > greatest:
        greatest = b
    if c > greatest:
        greatest = c

    return greatest

print(findGreatest(1,33,2))

def printStars(n):
    if n==0:
        return
    for i in range(1,n+1):
        print("*",end="")
    print()
    printStars(n-1)

printStars(3)

def printTables(n):
    for i in range(1,11):
        # You can use variables inside a string using this format.
        print(f"{n} X {i} = {n * i}")

printTables(5)

# Verify this solution from the video too.
mylist = ["apple"," banana", "mango ", " guava "]

def removeAndStrip(list,word):
    for item in list:
        item.strip()
    return list.remove(word)

print(removeAndStrip(mylist," guava "))

for item in mylist:
    print(item)