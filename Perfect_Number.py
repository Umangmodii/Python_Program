# Write a Program to Perfect Number

def main():
    print("Total Perfect Numbers Under 10000 : ", end='')
    for no in range(1, 10000):
        sm = 0
        for x in range(1, no):
            if no % x == 0:
                sm += x

        if no == sm:
            print(no, end=' ')

if __name__ == "__main__":
    main()