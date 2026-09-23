def main():
    start = 1
    end = int(input("What is the ending number?: "))

    # This solution is better, in the best-case scenario
    # if `start` is a number divisible by both 3 and 5,
    # the computer only has to evaluate the first IF
    # statement.
    # The worst-case scenario the computer evaluates 
    # the IF, ELIF, and the last ELIF which is if
    # `start` is a number divisible by 5 or is a number
    # not divisible by 3 and 5.
    # Remember the ELSE does not have any conditional,
    # so if the last ELIF evaluates to False, the computer
    # runs the ELSE statement.
    while start <= end:
        if start % 3 == 0 and start % 5 == 0:
            print("FizzBuzz")
        elif start % 3 == 0:
            print("Fizz")
        elif start % 5 == 0:
            print("Buzz")
        else:
            print(start)
        start += 1

    print("Program Terminated")

if __name__ == "__main__":
    main()