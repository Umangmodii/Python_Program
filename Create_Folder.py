# Create a New Folder in Python

import os

# f = "C:/Example"

# os.mkdir(f)

# if f:
#    print("Folders {0} Created Successfully!", f)
# else:
#    print("Folders are {0} not created!", f)

f1 = "C:/Example"
f = open("C:/Example/data.txt",'w')
f.write("My First Test Data!")
f.close()

f2 = open("C:/Example/data.txt",'r')
print(f2.read())
f2.close()

