n = int(input("Enter the Number : "))

# 1. Star Pyramid

# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *

for i in range(0,n):
    for j in range(0,i+1):
        print("* ", end=" ")
    print()

# 2. Five Star Print All

# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *

for i in range(0,n):
    for j in range(0,n+1):
        print("* ", end="")
    print()

# Pattern - 3: Printing Downward half - Pyramid

# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(0+1,0,-1):
    for j in range(0,i-1):
        print(" *", end="")
    print()




