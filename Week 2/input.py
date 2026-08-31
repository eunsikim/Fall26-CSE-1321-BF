def main():
    user_name = input("Enter your name: ")
    # Order of procedure:
    # 1. user_name = input("Enter your name: ")
    # 2. printing "Enter your name: "
    # 3. Wait for user input
    # 4. User enters: John
    # 5. input(...) evaluates as "John"
    # 6. user_name = "John"
    # *input() function will always return/evaluate as a String data type

    print("Hello ", end="")
    print(user_name)

if __name__ == "__main__":
    main()