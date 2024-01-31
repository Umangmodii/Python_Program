def Checkprime(no):
    for x in range(2, no):
        if no % x == 0:
            return False
    return True

def CheckPalin(no):
    rno = ""
    dno = no

    while no != 0:
        rem = no % 10
        rno = rno + str(rem)
        no = no // 10

    return True if str(dno) == rno else False

def main():
    for no in range(1, 1000):
        if Checkprime(no) and CheckPalin(no):
            print(no, end=" ")

if __name__ == "__main__":
        main()




