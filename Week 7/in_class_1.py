def get_letter_grade(grade):
    if grade > 89:
        return "A"
    elif grade > 79:
        return "B"
    elif grade > 69:
        return "C"
    elif grade > 59:
        return "D"
    else:
        return "F"

def main():
    number_grade = float(input("Enter a number grade: "))

    letter_grade = get_letter_grade(number_grade)

    print(f"{number_grade} is a {letter_grade}")

if __name__ == "__main__":
    main()