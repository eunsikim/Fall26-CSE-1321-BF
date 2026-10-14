# With this method of importing, we can choose specific functions to import
# and we do not need to refer to the file to use these functions
from my_function import hello_world, calculation

import my_math

def main():
    hello_world() # Notice we dont have `my_function.`

    print(calculation(10, n3 = 5))

if __name__ == "__main__":
    main()