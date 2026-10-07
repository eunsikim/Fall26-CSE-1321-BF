# Definition/Header of the function
def is_even(number): # def identifier/name(parameter(s)):
    # Body of the function
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is not even")

def add(n1, n2):
    # Scope: the variable calculation only exist within inside the function
    calculation = n1 + n2

    return calculation

def main():
    # # Function call
    # is_even(51) # identifier/name(argument(s))

    # for x in range(10):
    #     is_even(x)

    age = int(input("What is your age?: "))

    new_age = add(age, 10) # This function call is an expression of a number (resulting value of the calculation)

    print("10 years pass by...")
    print(f"You are {new_age} years old now.")

if __name__ == "__main__":
    main()