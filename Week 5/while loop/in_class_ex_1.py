# - Ask the user to input a number
# - The program should print a sequence from 1 to
#   the number the user inputs
# - If a number is divisible by 3, the program should
#   print "Fizz" instead of that number
# - If a number is divisible by 5, the program should
#   print "Buzz" instead of that number
# - If a number is both divisible by 3 and 5, the program
# should print "FizzBuzz" instead

"""
Sample Output:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
"""

def main():
    start = 1
    end = int(input("What is the ending number?: "))

    # This solution works, but it can be improved.
    # One of the cons in this solution is that
    # the computer must perform each of the IF 
    # statement conditions.
    # That is 4 conditions, and each condition 
    # contains 3 sub-conditions (the left hand
    # side expression, right hand side expression 
    # and the "AND" logical operation)
    # Thus, the computer has to perform 12 evaluation
    # for each number in the sequence
    # Check in_class_ex_1_var_2.py for the improved 
    # version 
    while start <= end:
        if start % 3 == 0 and start % 5 != 0:
            print("Fizz")
        if start % 5 == 0 and start % 5 != 0:
            print("Buzz")
        if start % 3 == 0 and start % 5 == 0:
            print("FizzBuzz")
        if start % 3 != 0 and start % 5 != 0:
            print(start)
        start += 1

    print("Program Terminated")

if __name__ == "__main__":
    main()