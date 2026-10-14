from sample import quiz_avg, input_grade, input_bonus, test_policy, final_grade, convert_letter_grade, print_grade

def main():
    print("Quizzes")
    quizzes = quiz_avg()

    print("\nTest 1")
    test_1 = input_grade()
    print("\nTest 2")
    test_2 = input_grade()
    print("\nFinal Exam")
    final = input_grade()

    print()

    final += input_bonus()
    test_1 = test_policy(t1 = test_1, t2 = test_2, f = final)
    test_2 = test_policy(t2 = test_2, f = final)

    grade_num = final_grade(quizzes, test_1, test_2, final)
    grade_let = convert_letter_grade(grade_num)

    print()

    print_grade(grade_num, grade_let)

if __name__ == "__main__":
    main()