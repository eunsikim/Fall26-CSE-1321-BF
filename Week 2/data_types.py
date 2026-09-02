def main():
    num1 = 40
    num2 = 3.5
    message = "Hello CSE 1321"

    # We can use the type() function
    # to check the data type of a value
    # at a determined time in the code
    print(num1, end=" is a ")
    print(type(num1))

    num1 = 40.0

    print(num1, end=" is a ")
    print(type(num1))

    num1 = "40.7"
    print(num1, end=" is a ")
    print(type(num1))

    print()

    # Data Conversions
    num1 = float(num1)
    # Step by step:
    # 1. num1 = float(num1)
    # 2. num1 = float("40.0")
    # 3. num1 = 40.0
    print(num1, end=" is a ")
    print(type(num1))

    # You can only convert values
    # that are valid
    # num1 = float("3.14!")

    # Any time you convert a float into an int
    # python will truncate the value meaning
    # it will remove the decimal portion of the number
    num1 = int(num1)
    print(num1, end=" is a ")
    print(type(num1))

    # Adding the decimal portion
    # back into num1
    num1 = float(num1)
    num1 = str(num1)
    print(num1, end=" is a ")
    print(type(num1))

    num1 = int(num1)
    print(num1, end=" is a ")
    print(type(num1))





if __name__ == "__main__":
    main()