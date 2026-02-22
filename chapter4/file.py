# List & tuples in Python.
# Like JavaScript has arrays, python has lists. Lists are mutable in java.
# Apply lists methods modifies & returns the same list.

fruits = ["apple","mango","litchi"]

print(fruits)

mylist = [43,1,6,38, 0]
randomList = ["fruits",33, True]

# print(mylist)
# mylist.sort()
# print(mylist)
# mylist.reverse()
# print(mylist)
# mylist.append(99)
# print(mylist)
# mylist.insert(1, 88)
# print(mylist)
# mylist.pop(5)
# print(mylist)
# mylist.remove(88)
# print(mylist)

# A tuple in Python is a built-in data type that allows you to create immutable sequences of values.
# It's like a immutable list.

a = (1)
print(type(a))
# To create a tuple with single element do it like this.
aa = (1,)
print(type(aa))

my_tuple = (1,2,3,1,74, False,"random",23)
b = (1,2,3,1,74,23)
print(b)

print(b.count(1))
print(b.index(74))
print(len(b))
print(max(b))
print(sum(b))
print(min(b))

print(99 in b)
print("randomm" in my_tuple)
print("random" in my_tuple)

marks = []

# s1 = input("enter marks ->")
# marks.append(int(s1))
# s2 = input("enter marks ->")
# marks.append(int(s2))
# s3 = input("enter marks ->")
# marks.append(int(s3))
# s4 = input("enter marks ->")
# marks.append(int(s4))
# s5 = input("enter marks ->")
# marks.append(int(s5))
# s6 = input("enter marks ->")
# marks.append(int(s6))

# marks.sort()
# print(marks)

list = [1,55,33,322]
print(sum(list))

test = (7, 0, 8, 0, 0, 9)
print(test.count(0))