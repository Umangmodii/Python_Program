# create-a-vector-in-python-using-numpy

import numpy as no

a = [10,20,30,40,50]
b = [15,25,35,45,55]

v1 = no.array(a)
v2 = no.array(b)

print("We create vector from a list 1")
print(v1)

print("We create vector from a list 2")
print(v2)

add = v1 + v2

print("Addition of two vectors:",add)
