def get_user_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    return name, age
    # return (name, age)

def calculate_avg(*grades):
    grades_sum = 0

    for grade in grades:
        grades_sum += grade

    return grades_sum / len(grades)

def main():
    # user_info_tuple = get_user_info()
    # print(f"Hello {user_info_tuple[0]}, you are {user_info_tuple[1]} years old.")

    name, age = get_user_info()
    print(f"Hello {name}, you are {age} years old.")

    print(f"Grade Average: {calculate_avg(80, 98, 100, 75, 84)}")



if __name__ == "__main__":
    main()