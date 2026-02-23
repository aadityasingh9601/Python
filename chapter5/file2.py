# SETS IN PYTHON

# Set is a collection of non-repetitive elements. Immutable & unindexed in python.

nz = {} # type is disctionary
emptySet = set()

s = {1,3,4,1}
print(type(emptySet),type(s))
print(emptySet)
print(s)

s.add(44)
print(s)

s.remove(1)
print(len(s))
print(s)

r = s.copy()
print(type(r))
print(r)
r.clear()
print(r)

# Union & Intersection in Sets

s1 = {1,4,3,2,99}
s2 = {3,5,88,77}

print(s1.union(s2))
print(s1.intersection(s2))


n = set()

n1 = input("enter number -> ")
n.add(int(n1))
n2 = input("enter number -> ")
n.add(int(n2))
n3 = input("enter number -> ")
n.add(int(n3))

print(n)

test = set()
test.add(3) # Int
test.add('3') # String
test.add(3.0) # Float
# This will print 2 because python doesn't care about the data type of the input if the values of both of them are equal
# Here, value of 3 & 3.0 are same, so counted as one.
print(len(test))
