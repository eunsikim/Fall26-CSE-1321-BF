def main():
    print("`range()` sequence")
    print(list(range(5))) # End range is always EXCLUSIVE

    print()

    print("`range()` with single param")
    # Range function with a SINGLE paramater:
    # `range(X)`
    # Start range is always 0 Inclusive
    # End range is X exclusive
    for number in range(10):
        print(number)

    print()

    print("`range()` with double param")
    # Range function with TWO paramaters:
    # `range(x, y)`
    # Start range is X Inclusive
    # End range is Y Exclusive
    for number in range(4, 10):
        print(number)
        
if __name__ == "__main__":
    main()