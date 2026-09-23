def main():
    user_choice = ""

    while user_choice != "Q": # We have defined "Q" as a sentinel value
        print("Choose an option:")
        print("1 - Print Hello World")
        print("Q - To Quit")
        user_choice = input("> ")

        if user_choice == "1":
            print("Hello World")
        elif user_choice == "Q":
            print("Stopping the program...")
        else:
            print("Please enter one of the options. Try again.")

    print("Program Terminated")

if __name__ == "__main__":
    main()