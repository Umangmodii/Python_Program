# Create a Tuples

tuple = (10,20,30,40,50)
count = 0

for i in tuple:
    print("Tuples Values is [%d] = %d" % (count, i))
    count = count + 1

# User Input the Tuples

# tuple1 = tuple(input("Enter the Tuples Elements : "))
#print(tuple1)
#counts = 0

#for j in tuple1:
#    print("tuples Values is [%d] = [%s]" % (counts, j))
#    counts = counts + 1

# Index Values in Tuples

tup = (0,1,2,3,4,5)

for i in tup:
    print("The Tupeles Index Values is : ",i)

# Positive Indexing // Left to Right Side

t1 = (1,2,3,4,5,6)

print(t1[:])
print(t1[1:])
print(t1[3:5])
print(t1[5:6:1])
print(t1[1:5])

# Negative Indexing // Right to Left Side // Index Values is -1 Means 1

t2 = (1,2,3,4,5)

print(t2[-1])
print(t2[-4])
print(t2[-3:-1])
print(t2[-2:])

# Delete a Tuples // Not a Support the Delete Records.

t3 = (1,2,3,4,5,6)

del t3[1]
print(t3)



