# Create a Single Inheritance

# Base Class
class parent:
    def fun1(self):
        print("The Class is Parent!")

# Derived class
class child(parent):
    def fun2(self):
        print("The Class is Child!")

c1 = child()
c1.fun1()
c1.fun2()

# Create a Multiple Inheritance

# Base Class
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

# Base Class
class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

# Derived Clas
class son(Mother,Father):

    def parent(self):
        print("Mother Name is : ",self.mothername)
        print("Fathe Name is : ",self.fathername)

# Creating a Derived Class Objects

s1 = son()
s1.mothername = "Pinkeyben"
s1.fathername = "Chandrakant"
s1.parent()








