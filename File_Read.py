f = open("C:\LICENSE.txt","r")
print(f.read())
f.close()

if f:
    print("File is Opened.")
else:
    print("File is Not Opened.")