# While loop

a = 1

while a <= 50:
    print(a)
    a = a + 1

# For loop

items = ["apple","mango","banana"]

for item in items:
    print(item)

#  Used to generate a sequence of number. 
for i in range(1,11):
    if i==2:
        continue
    print(i)
    if i==5:
        break
else:
    print("Dont printing!")


# pass instructs to do nothing at all.
l = [1,5,3,4]
for item in l:
    pass


l = ["Harry", "Soham", "Sachin", "Rahul"]

for person in l:
    if (person[0] == "S"):
        print("Hello", person)

n = 1
sum = 0

while n <= 100:
    sum = sum + n
    n = n+1

print(sum)

i = 1

while i <=3:
    if i==2:
        print("* *")
    else:
        print("***")
    i = i+1


for a in range(1,4):
    for b in range(1,a+1):
        print("*", end="") # Printing something in the same line.
    print()

n = 3
for c in range(1,n+1):
    s = n - c
    d = (2 * c) - 1
    
    for s in range(1,n-c+1):
        print(" ",end="")
    for d in range(1,2*c):
        print("*",end="")
    
    print()

# Check if number is prime or not.
# Prime number -> Number which divides by 1 or itself.

n = int(input("Enter your number -> "))

for i in range(2,n):
    if (n % i == 0):
        print("No, it's not a prime number!")
        break
else:
    print("Yes, it's a prime number!")