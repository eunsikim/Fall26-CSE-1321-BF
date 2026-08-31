def main():
    user_name = input("Enter your name: ")
    user_year_born = int(input("Enter your birth year: "))
    # Order of operation
    # 1. user_year_born = int(input("Enter your birth year: "))
    # 2. print "Enter your birth year: "
    # 3. wait for user input
    # 4. user enters 1996
    # 5. The expression input(...) evaluates to "1996" (it is a string)
    # 6. We evaluate the int() as int("1996")
    # 7. We convert "1996" (string) into a number 1996 (int)
    # 8. assign user_year_born with the numeric type value 1996
    #       or: user_year_born = 1996

    age = 2026 - user_year_born

    print("Hello ", end="")
    print(user_name)

    print("You are ", end="")
    print(age, end=" ")
    print("years old")

if __name__ == "__main__":
    main()