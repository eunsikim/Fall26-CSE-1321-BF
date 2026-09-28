# Create a program that generates a python script
#
# The program should ask the user for two integers
# The program should generate print statements with
# the multiplication table of the first number
# The multiplication table will go from 0 to the second 
# input
#
# If the first input is 2, and the second input is
# 5, the multiplication table should be:
# 0 x 2 = 0
# 1 x 2 = 2
# 2 x 2 = 4
# ...
# 5 x 2 = 10
#
# YOU MUST USE A LOOP, no forced print statements
#
# output:
# print("0 x 2 = 0")
#
# HINT: print('"hello"') => OUTPUT: "hello" OR print("\"hello\"") => OUTPUT: "hello"

def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    print("Copy the lines of code below:")

    for x in range(num2 + 1): # range(0, num2 + 1)
        print(f"print(\"{x} x {num1} = {x * num1}\")")


if __name__ == "__main__":
    main()