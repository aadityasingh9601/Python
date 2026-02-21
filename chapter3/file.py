# Strings are immutable in Python

str = "asian Elephant" 

strLength = len(str)
print(strLength)
print(str,str[0])

print(str[1:4])
print(str[-4: -1])
print(str[2:-1])
print(str[: strLength ])

# Slicing with skip value

print(str[0:strLength:2]) #Print the string from 0 to strLength index & print each 2nd element

print(str.endswith("ant"))
print(str.count("a"))
print(str.capitalize())
print(str.find("an"))
print(str.replace("an","pt"))

#Escape sequence characters.
print(str,"\n",str)
print("\t",len(str),"\n",str)
print("\\")
print("\'")

# username = input("enter your name -> ")
# print("Good afternoon, " + username)

# date = input("Enter date -> ")

# letter = '''
#    Dear, <| username |>
#    You are selected
#    on date <| date |>
# '''

# print(letter.replace("<| username |>",username).replace("<| date |>",date))

testStr = "This  is  for  test"


print(testStr.count("  "))
print(testStr)
print(testStr.replace("  "," "))