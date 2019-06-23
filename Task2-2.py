def arrayMin(num, query, n):
    k = 0
    large = 0
    while k < query:
        index1 = int(input("enter the 1st index:"))
        index2 = int(input("enter the 2nd index:"))
        total = int(input("enter the value to be addded:"))
        j = index1
        while j <= index2:
            num[j] += total
            if num[j] > large:
                large = num[j]
            j += 1
        k += 1

    if large > num[n]:
        return large
    else:
        return num[n]


def main():
    num = []
    n = int(input("enter the length of array:"))
    query = int(input("enter the no of queries:"))
    for i in range(n+1):
        num.append(i)
    print(arrayMin(num, query, n))


if __name__ == "__main__":
    main()
