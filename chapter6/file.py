# if else in Python

condition1 = False
condition2 = True

if(condition1):
    print("Yes")

elif(condition2):
    print("No")

else:
    print("Maybe")

# age = int(input("Enter your age -> "))

# if(age >= 18):
#     print("You are an adult!")
# else:
#     print("You are not an adult!")

# greatest = 0

# n1 = int(input(""))
# if(n1 > greatest):
#     greatest = n1
# n2 = int(input(""))
# if(n2 > greatest):
#     greatest = n2
# n3 = int(input(""))
# if(n3 > greatest):
#     greatest = n3
# n4 = int(input(""))
# if(n4 > greatest):
#     greatest = n4

# print(greatest)

comment = "Hello"

if(comment == "Make lot of money" or comment == "click this" or comment == "subscribe this"):
    print("It's a scam!")
elif(comment == "Hello" or comment == "Bye"):
    print("It's not a scam!")
else:
    print("It's just a msg")


list = ["first","second","third"]
username = input("enter your name -> ")

if username in list:
    print("yes it's present")
else:
    print("no it's not present")


post = input("enter your post")

if ("Animal".lower() in post.lower()):
    print("Yes, it's talking about animal!")
else:
    print("No, it's not talking about animal!")