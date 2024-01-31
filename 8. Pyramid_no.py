# Practical 8 Pyramid Numbers

def main():
    no = int(input("Enter the No (0-9) : "))

    for i  in range(1,no+1):
        for j in range(no,i,-1):
            print(" ", end='')
        for j in range(1, i+1):
            print(j, end='')
        for j in range(i-1,0,-1):
            print(j, end='')

        print()

if __name__ == "__main__":
    main()