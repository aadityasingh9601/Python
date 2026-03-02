# import random
import shutil
import filecmp
import os

# with open("poems.txt","r") as q1:
#     text = q1.read()
#     print(text)
#     print(type(text))
#     index = text.find("twinkle")
#     if index == -1:
#         print("NO, twinkle doesn't exists!")
#     else:
#         print("Yes, poem has twinkle!")


# def game():
#     return random.choice([1,2,3,4,5])

# userScore = game()

# with open("Hi-score.txt","r+") as q2:
#     highScore = q2.read().strip() or "0" # Moves cursor to the end of file
#     q2.seek(0) # Move the cursor to the starting, else write will act like append because of cursor position.
#     if  (userScore > int(highScore)):
#         q2.write(str(userScore))
#         print(f"The new highScore is {userScore}")
#     else:
#         print(f"Your score is {userScore} & highest score is {highScore}")


# Writing multiplication tables & saving them to different files inside a folder.

# def printTable(n):
#     table = ""
#     for i in range(1,11):
#         table  = table + f"{n} X {i} = {n*i} \n"
#     return table

# for i in range(2,21):
#     file_name = f"./tables/{i}.txt"
#     with open(file_name,"w") as file:
#         file.write(printTable(i))


# Replace occurence of a particular word with a new word.

# with open("donkey.txt","r+") as file:
#     content = file.read()
#     updated_content = content.replace("donkey","######")
#     file.seek(0) # Bring pointer to the start
#     file.write(updated_content)

# Check if a file contains python or not.

# with open("log.txt","r") as file:
#     content = file.read()
#     if "python" in content:
#         print("Yes python exists!")
#     else:
#         print("No python doesn't exits!")

# Check on which line python exists.
# with open("log.txt","r") as file:
#     content = file.readlines()
#     for row in content:
#         word = "python"
#         if row.find(word) != -1:
#             print("Yes python exists!")
#             print(content.index(row))
#         else:
#             print("No python doesn't exits!")

# shutil.copy("./tables/2.txt","./copied.txt")

# if filecmp.cmp("./tables/2.txt","./copied.txt",shallow=False):
#     print("Yes, identical!")
# else:
#     print("No, they're not identical!")

# Clear content of a file.
with open("copied.txt","w"):
    pass

# Rename a file in Python
os.rename("./copied.txt","renamed_copied.txt")