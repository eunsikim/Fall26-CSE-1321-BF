def main():
    grades = [95.6, 81.5, 70.0]

    print("Choose an index value:")
    for index in range(len(grades)):
        print(f"{index} - {grades[index]}")

    index_choice = int(input("> "))

    new_grade = float(input("Enter new grade: "))

    print()

    # We can update values by the index
    grades[index_choice] = new_grade
    
    print(grades)

if __name__ == "__main__":
    main()