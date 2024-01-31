import random

otp = random.randint(000000,100000) # Random Number Generate
username = input("Enter the Username : ") # User Input Values
print("Hello : ",username)
print("Here is your OTP : ",otp)
password = input("Enter the otp to login: ")

if(password == str(otp)):
    print("User Successfully Login!")
else:
    print("Invalid Users!")


