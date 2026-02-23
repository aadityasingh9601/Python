# Like JavaScript has objects, Python has Dictionaries.

mydictionary = {
    "name" : "random",
    "age":20,
    "skills": ["React","Nextjs","Node.js","Express.js"]
}


print(type(mydictionary))
print(mydictionary.get("name"))
mydictionary["age"] = 21
print(mydictionary.get("age"))
print(mydictionary.get("skills")[3])
print(mydictionary.keys())
print(mydictionary.items())
mydictionary.update({"name":"monster"})
print(mydictionary)
print(mydictionary.pop("age"))
print(mydictionary)

# print(mydictionary.get("name2")) # Returns none
# print(mydictionary["name2"]) # Returns an error
mydictionary.clear()

print(mydictionary)

fruits = {
    "kela":"banana",
    "seb":"apple"
}

print(fruits.get("kela"))
print(fruits.get("seb"))