def main():
    array = [35, 10, 31, 11, 26]
    print("Before sorting Element array are -")

    for i in array:
        print(i, end = " ")
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    print("\n After Sorting Element array are -")

    for i in array:
        print(i, end=" ")

if __name__ == '__main__':
    main()