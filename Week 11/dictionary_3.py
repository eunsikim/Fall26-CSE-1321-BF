def main():
    grades = {
        # Key : Value
        "Syllabus Quiz":100.0,
        "Quiz 1": 87.0,
        "Quiz 2": 98.0,
        "Test 1": 95.6,
        "Final Exam": 105.0
    }

    for x in grades:
        print(x)

    print()

    for key in grades:
        print(grades[key])

    print()

    for value in grades.values():
        print(value)

    print()

    for entry in grades.items():
        print(entry)

    print()

    for key in grades.keys():
        print(key)

    
    
if __name__ == "__main__":
    main()