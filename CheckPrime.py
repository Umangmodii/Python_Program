# Write a Program that reads an integer and displays all its

def CheckPrime(p):
    for x in range(2, p):
        if p % 2 == 0:
            return  False

    return True

def main():
    no = int(input("Enter any Number : "))
    print("Total Number are : ", end='')
    for x in range(1, no):
       if no % x == 0 and CheckPrime(x):
           print(x, end=' ')



if __name__  == "__main__":
    main()