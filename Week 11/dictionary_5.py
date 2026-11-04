def main():
    # Using a dictionary to keep track of a single student's grade
    grades = {
        "Quiz": [],
        "Test": [],
        "Final Exam": 0
    }

    for x in range(11):
        if x == 0:
            grade = float(input(f"Enter grade for Syllabus quiz: "))
        else:
            grade = float(input(f"Enter grade for Quiz {x + 1}: "))

        grades["Quiz"].append(grade)

    print(grades["Quiz"])

    # Using a dictionary to keep track of grades of all students
    students = {
        "John Doe" : {
            "Quiz": [],
            "Test": [],
            "Final Exam": 0
        },
        "Alice" : {
            "Quiz": [],
            "Test": [],
            "Final Exam": 0
        },
        "Bob" : {
            "Quiz": [],
            "Test": [],
            "Final Exam": 0
        }
    }

    students["John Doe"]["Quiz"].append(89)

    print(students)
    
if __name__ == "__main__":
    main()