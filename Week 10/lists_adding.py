import time

def main():
    # Initializing an empty list
    grades = []

    print(grades)

    # `append()` adds an object to end of the list
    grades.append(90)
    print(grades)

    grades.append(85)
    print(grades)

    # `insert()` adds an object to a specific index
    grades.insert(0, 95)
    print(grades)


    grades.insert(5, 95) # The computer will add 95 to the next available index
    print(grades)

if __name__ == "__main__":
    main()