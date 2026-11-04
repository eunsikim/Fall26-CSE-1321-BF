def main():
    sample_dictionary = {}

    grades = {
        # Key : Value
        "Syllabus Quiz":100.0,
        "Quiz 1": 87.0,
        "Quiz 2": 98.0,
        0: "Zero",
        3.14:[10, "ten", 10.0],
        # [10]:"This should not work", # Keys must be immutable, this will break
        (10):"Testing"
    }

    print(grades["Syllabus Quiz"])
    print(grades["Quiz 1"])
    print(grades[0])
    print(grades[3.14])
    print(grades[(10)])
    
if __name__ == "__main__":
    main()