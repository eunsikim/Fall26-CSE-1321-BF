"""
Number categorizer:
- Prompt the user for a number.
- The program should evaluate if the number is negative 
  or zero. If neither, it should check if the number 
  is even or odd.
"""

def main():
    number = int(input("Enter a number: "))

    if number < 0:
        print(f"{number} is negative")
    elif number == 0:
        print(f"{number} is zero")
    else: # number MUST be positive
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")

    print("Program Terminated")

if __name__ == "__main__":
    main()