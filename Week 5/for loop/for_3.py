# The program should count how many vowels 
# the variable `message` has.
# DO NOT USE THE `len()` FUNCTION.

def main():
    message = "HEllo World"

    vowel_count = 0

    message = message.lower()

    for character in message:
        # character == "a" or "e" or "i" or "o" or "u" THIS IS ILLEGAL
        if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
            vowel_count += 1

    print(f"'{message}' has {vowel_count} vowels")



if __name__ == "__main__":
    main()