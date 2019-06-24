def arrayMin(num, query, n):
    k = 0
    large = 0
    while k < query:
        index1, index2, total = map(int, input().split())
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
    n = int(input(""))
    query = int(input(""))
    for i in range(n+1):
        num.append(i)
    print(arrayMin(num, query, n))


if __name__ == "__main__":
    main()

