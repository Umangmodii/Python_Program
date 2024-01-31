list1 = [1,2,3,4,5,6,7,8,10]
# new_list = [i in range(list1) and j in range(list2) if list1 % 2 == 0]

new_list = (i for 1 in list1 if i % 2 == 0)

print(new_list)