def double(x):
    return x * 2


def quadruple(x):
    return x * 4


def getOddNumber(k, getEvenNumber):
    return 1 + getEvenNumber(k)


def main():
    k = 1
    i = getOddNumber(k, double)
    print(i)

    i = getOddNumber(k, quadruple)
    print(i)

    i = getOddNumber(k, lambda x: x * 8)
    print(i)


if __name__ == "__main__":
    main()
