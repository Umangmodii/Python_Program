# Recursion Find the Factorial Numbers

def fact(n):

    # Base Case means What : Number of n time and break the Statements.

    if n == 0:     # Linear Time Complexity is : 0(n)
        return 1

    # Function Return the : Fact(n)

    return n * fact(n-1)   # Factorial Time Complexity is : 0(n!)

def main():

    # User takes the Input Values

    n = eval(input("Enter the Factorial Number :"))      # Linear Time Complexity is : 0(n)
    ans = fact(n)

    print("The Factorial Number is : {0}".format(ans))


if __name__ == '__main__':
    main()











