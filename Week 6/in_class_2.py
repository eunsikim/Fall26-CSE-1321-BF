# Create program that takes in two integers
# and then output the sum of the two numbers
# 
# You are allowed to use the addition operator 
# `+` but only with the integer 1
# 
# 1 + 1 => 1 + 1
# 2 + 3 => 1 + 1 + 1 + 1 + 1 = 5
# 4 + 2 => 1 + 1 + 1 + 1 + 1 + 1 = 6

def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    addition = 0

    for x in range(num1):
        addition += 1

    for x in range(num2):
        addition += 1

    print(f"{num1} + {num2} = {addition}")

if __name__ == "__main__":
    main()