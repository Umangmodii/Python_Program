# Write a Menu Driven Program Binary, Octal and HexaDecimal.

def d2b(no):
    bn = ''
    while no != 0:
        rem = no % 2
        bn = str(rem) + bn
        no =  no // 2
        return bn

def d2o(no):
    bn = ''
    while no !=0:
        rem = no % 8
        bn = str(rem) + bn
        no = no // 2
        return bn

def d2x(no):
    hx = ''
    while no !=0:
        rem = no % 16
        match rem:
            case 10:
                hx = "A" + hx
            case 11:
                hx = "B" + hx
            case 12:
                hx = "C" + hx
            case 13:
                hx = "D" + hx
            case 14:
                hx = "E" + hx
            case 15:
                hx = "F" + hx
            case default:
                bn = str(rem) + hx
        no = no // 16
        return hx

def main():
    ans = 0

    while True:
        print("0. Input Decimal Value : ")
        print("1. To Decimal : ")
        print("2. To Octal : ")
        print("3. To HexaDecimal : ")
        print("4. Exit : ")

        ans = int(input("Enter your choice :"))
        match ans:
            case 0:
                dno = int(input("Enter the Decimal Number : "))

            case 1:
                # print("Decimal {0} has Binary {1}".format(dno, d2b(dno)))
                print("Decimal {0} has Binary {1}".format(dno, bin(dno)))

            case 2:
                #  print("Decimal {0} has Octal {1}".format(dno, d2o(dno)))
                print("Decimal {0} has Binary {1}".format(dno, oct(dno)))

            case 3:
                # print("Decimal {0} has HexaDecimal {1}".format(dno, d2x(dno)))
                print("Decimal {0} has Binary {1}".format(dno, hex(dno
                                                                   )))

            case 4:
                break

            case default:
                print("Invalid Values")

if __name__ == '__main__':
    main()










