# Using Python List comprehension

List = ['wood', 'oil', 'apple', 'bat', 'iron', 'Apple2']
for i in List:
    vowels = [i for i in List if i[0] in "aeiouAEIOU"]
    print(vowels)
