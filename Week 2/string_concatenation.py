# This is an update of input_2.py
def main():
    user_name = input("Enter your name: ")
    user_year_born = int(input("Enter your birth year: "))

    age = 2026 - user_year_born

    # Concatenation
    print("Hello " + user_name)

    # You can only concatenate strings with other strings
    # print("You are " + age + " years old") # commented because it will crash

    print("You are " + str(age) + " years old")
    # Order of execution
    # 1. print("You are " + str(age) + " years old")
    # 2. print("You are " + str(30) + " years old") # assuming the user inputted 1996 for birth year
    # 3. print("You are " + "30" + " years old")

if __name__ == "__main__":
    main()