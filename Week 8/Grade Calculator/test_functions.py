def input_grade():
    grade = int(input("Enter your grade: "))
    while True:
        if 0 <= grade <= 100:
            return grade
        else:
            grade = int(input("Enter your grade: "))


def check_lowest(g1, g2):
    if g1 < g2:
        return g1
    elif g1 > g2:
        return g2




# print(input_grade())
print(check_lowest(5, 80))
print(check_lowest(80, 90))