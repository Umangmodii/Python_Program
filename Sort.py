sort = [1,3,2,6,7,8,5,4]

for i in range(len(sort)): # Total Number of Length
    for j in range(i+1,len(sort)):  # Total Number of Length
     if sort[i] > sort[j]:  # i greater than j
        sort[i],sort[j] = sort[j],sort[i]  # Swapping Value i and j
print("The Sorted List is : {0}".format(sort))  # Print the Message








