n = eval(input("Enter the Number : "))
reverse = 0

while(n > 0):
    r = n % 10
    reverse = (reverse * 10) + r
    n = n // 10

print("The Reverse Number is : {0} ".format(reverse))