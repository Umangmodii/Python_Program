# a = 10
# print (type("a"))

# Tuples, List and dictionary

a = (10,20,30,40,50) # Tuples
b = [10,20,30,40,50] # List
d = {"I":1, "Love":2, "You":3}
c = 10.0

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Change Tuples

x = ("Red","Green","Blue")
y = list(x)
y[1] = "Yellow"
x = tuple(y)

print(x)

# Remove Tuples

x = ("Red","Gren","Blue")
y = list(x)
y.remove("Red")
x = tuple(y)

print(x)

# Dictionary Find Keys & Values

dictionary = {
     "id": "1",
     "name": "Umang",
     "DOB": "15-01-2003",
     "City": "Patan"
}

for key,value in dictionary.items():
    print(key," : ",value[1])


