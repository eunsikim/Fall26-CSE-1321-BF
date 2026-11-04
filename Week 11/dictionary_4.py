def main():
    grades = {
        # Key : Value
        "Syllabus Quiz":100.0,
        "Quiz 1": 87.0,
        "Quiz 2": 98.0,
        "Test 1": 95.6,
        "Final Exam": 105.0,
    }

    # This boolean expression will be False becase
    # we do not have `98.0` as a key
    if 98.0 in grades:
        print("98.0 exists in grades")
    else:
        print("98.0 does not exists in grades")

    if "Quiz 1" in grades:
        print("Quiz 1 exists in grades")
    else:
        print("Quiz 1 does not exists in grades")

    if 98.0 in grades.values():
        print("98.0 exists in grades")
    else:
        print("98.0 does not exists in grades")

    if ("Test 1", 95.6) in grades.items():
        print("(\"Test 1\", 95.6) exists in grades")
    else:
        print("(\"Test 1\", 95.6) does not exists in grades")
    
    if ("Test 1", 100.0) in grades.items():
        print("(\"Test 1\", 100.0) exists in grades")
    else:
        print("(\"Test 1\", 100.0) does not exists in grades")


    
    
if __name__ == "__main__":
    main()