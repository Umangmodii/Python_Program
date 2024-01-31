# Adding a Elements to the List

l = []

n = int(input("Enter the Number of Elements in the List : "))
for i in range(0,n):
    l.append(input("Enter the Item in List : "))
print("Printing the list items.....")

for i in l:
    print(i, end=" ")

# Remove a Elements to the List

l1 = [0,1,2,3,4,5]

print("Printing original list....")
for i in l1:
    print(i, end=" ")
l1.remove(3)

print("Printing the list after the removal of first elements.....")

for i in l1:
    print(i, end=" ")

# Sum of List

l2 = [10,20,30,40,50]
sum = 0

for i in l2:
    sum = sum + i

print("The Sum is : {0}".format(sum))

# List of Common one Values

list1 = [1,2,3,4,5]
list2 = [0,6,7,8,4]

for x in list1:
    for y in list2:
        if x == y:
            print("The common elements is : {0}".format(x))



