def main():
    grades = [95.6, 81.5, 70.0, 55.7, 70.0, 100.0]

    print(len(grades))
    print(max(grades))
    print(min(grades))

    print(grades.count(70.0))

    print(grades)

    grades.reverse()
    
    print(grades)

    grades.sort()

    print(grades)

    grades.sort(reverse=True)

    print(grades)

    names = ["Bob", "Jack", "John", "Tim", "Joey", "1", "2", "10"]

    print(names)

    names.sort()

    print(names)


if __name__ == "__main__":
    main()