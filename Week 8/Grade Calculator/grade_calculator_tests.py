def input_grade():
    while True:
        grade = float(input("Enter grade: "))

        if grade >= 0 and grade <= 100:
            return grade
        else:
            continue

def check_lowest(grade1, grade2):
    if grade1 < grade2:
        return grade1
    else:
        return grade2

def quiz_avg():
    lowest_grade = 100

    grade_sum = 0

    for i in range(3): 
        quiz_grade = input_grade()

        grade_sum += quiz_grade

        lowest_grade = check_lowest(lowest_grade, quiz_grade)

    grade_sum -= lowest_grade

    return grade_sum / 2

def test_policy(test_1 = False, test_2 = False, final = False):
    if test_1 != False: # If test_1 is a grade value [0, 100]
        if test_1 > test_2 and test_1 > final:
            return test_1
        elif test_2 > test_1 and test_2 > final:
            return test_2
        else:
            return final
    elif test_1 == False:
        if test_2 > final:
            return test_2
        else:
            return final

# def input_bonus():
#     visits = int(input("How many times have you visited the tutoring center?: "))

#     if visits <= 0:
#         return 0
#     elif visits >= 10:
#         return 5
#     else:
#         return visits * 0.5


# def input_bonus():
#     count = int(input("How many times have you been to the tutoring center: "))

#     if count > 10:
#         count = 10

#     points = count * 0.5
#     return points

def input_bonus():
    tutor = float(input("How many times have you been to the tutoring center?: "))
    points = tutor * 0.5
    if points > 5.0:
        print("You get 5.0 bonus points")
        return 5.0
    else:
        print(f"You get {points} bonus points")
        return points
    

