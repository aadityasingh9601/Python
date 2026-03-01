# File I/O.

# Opening a file in read mode
f = open("file.txt","r")
# Read the file contents.
content = f.read()
print(content)
# Print first line of the file.
# print(f.readline()) 
# Close the file.
f.close()

# Open a file in write mode.
f2 = open("file.txt","w")
print(f2)
f2.write("This is the new line!")
f2.close()

# Open a file in append mode.
f3 = open("file.txt","a")
f3.write("\n This line needs to be appended")
f3.close()

# With statement
# Opens the file in append mode using "with" statement, which automatically closes the file
with open("file.txt","a") as myfile:
    myfile.write("\n This new line also needs to be added into our file!")
    
