def main():
    test_list = [10, 20, 30]

    grades = {
        # Key : Value
        "Syllabus Quiz":100.0,
        "Quiz 1": 87.0,
        "Quiz 2": 98.0,
        "Test 1": 95.6,
        "Final Exam": 105.0
    }

    print(grades)
    print()

    # Adding Item/Entries 
    print("Adding Test 2 with 86.2")
    grades["Test 2"] = 85.2
    print(grades)
    print()

    # Modify/Update an entry
    print("Modifying Test 1 with 105.0")
    grades["Test 1"] = 105.0
    print(grades)
    print()

    # Removing an entry
    print("Removing with the DEL statement")
    del grades["Test 2"]
    print(grades)
    print()

    print("Removing with .pop(\"Test 1\")")
    print(grades.pop("Test 1"))
    print(grades)
    print()

    print("Removing with .popitem()")
    print(grades.popitem())
    print(grades)
    print()

    print("Removing all entries with .clear()")
    grades.clear()
    print(grades)
    print()


    
if __name__ == "__main__":
    main()