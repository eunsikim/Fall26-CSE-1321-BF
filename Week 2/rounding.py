def main():
    num1 = 3.3

    print(round(num1))

    num1 = 3.7

    print(round(num1))

    # 3.5 will round up to 4
    num1 = 3.5

    print(round(num1))

    # 2.5 will round down to 2
    num1 = 2.5

    print(round(num1))

    # the round() function will
    # always round (for half numbers)
    # to the nearest even number

if __name__ == "__main__":
    main()