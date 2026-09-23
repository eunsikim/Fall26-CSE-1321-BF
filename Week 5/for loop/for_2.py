# The program should count how many characters 
# the variable `message` has.
# DO NOT USE THE `len()` FUNCTION.

def main():
    message = "Hello World"

    count = 0

    for character in message:
        count += 1

    print(f"'{message}' has {count} characters.")

if __name__ == "__main__":
    main()