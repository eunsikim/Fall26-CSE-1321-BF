def main():
    age = int(input("Enter your age: "))

    if age >= 21:
        print("You are allowed to drink and vote")
    elif age >= 18:
        print("You are allowed to vote")
    else:
        print("You are not allowed to drink or vote")

    print("Program Terminated")

if __name__ == "__main__":
    main()