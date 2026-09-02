# This is an update of input_2.py
def main():
    user_name = input("Enter your name: ")
    user_year_born = int(input("Enter your birth year: "))

    age = 2026 - user_year_born

    print(f"Hello {user_name}")
    print(f"You are {age} years old.")

if __name__ == "__main__":
    main()