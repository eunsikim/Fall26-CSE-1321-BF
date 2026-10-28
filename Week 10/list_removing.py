def main():
    grades = [95.6, 81.5, 70.0, 55.7, 70.0, 100.0]

    print("Printing `grades` before any removal")
    print(grades)

    # Removing by Index:
    print("Deleting value at index 0")
    del grades[0]

    print(grades)

    print("Popping value at index 0")
    deleted_grade = grades.pop(0)
    print(f"{deleted_grade} just got deleted from the grade list")

    print(grades)

    # Removing by Value:
    print("Removing the first occurence of 70.0 in the grades list")

    grades.remove(70.0)

    print(grades)

    print("Clearing the grades list...")

    grades.clear()

    print(grades)

if __name__ == "__main__":
    main()