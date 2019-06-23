def parser(string):
    openBracket = []
    length = 0
    for j in string:
        if j == "<":
            openBracket.append(j)
        elif j == ">":
            if len(openBracket) == 0:
                return length
            elif len(openBracket) != 0:
                openBracket.pop()
                length += 2

    return length


def main():
    num = int(input("enter the no of strings:"))
    strings = []
    for x in range(num):
        x = str(input("enter the strings "))
        strings.append(x)

    for string in strings:
        print(parser(string))


if __name__ == "__main__":
    main()
