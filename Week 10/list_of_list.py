def main():
    # ["Bob", "Jack", "John", "Tim", "Joey"]
    single_student = ["Bob", 80.7]

    student_list = [
        ["Bob", 80.7, [70, 89]],
        ["Jack", 94.5],
        ["John", 97.5],
        ["Tim", 30.4],
        ["Joey", 70.5]
    ]

    print(student_list[2][0])

    print(f'{student_list[2][0]} got a {student_list[2][1]} on Test 1')

    # With this print statement we can access
    # the sublist inside the sublist 0 on student_list
    print(f'{student_list[0][2][0]}')
    
    print()

    # Traversal by Value:
    for student in student_list:
        print(f'{student[0]} got a {student[1]} on Test 1')
    
    print()

    # Traversal by Index:
    for x in range(len(student_list)):
        print(f'{student_list[x][0]} got a {student_list[x][1]} on Test 1')
    
    print()

    for x in range(len(student_list)):
        for y in range(len(student_list[x])):
            print(student_list[x][y], end=" ")
        print()

if __name__ == "__main__":
    main()