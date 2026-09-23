# The program should count how many vowels,
# consonants, empty spaces, and characters 
# the variable `message` has.
# DO NOT USE THE `len()` FUNCTION.

# Assume `message` will only contain
# Alphabetic characters and empty/blank spaces

def main():
    message = "HEllo World"

    message = message.lower()

    char_count = 0
    vow_count = 0
    cons_count = 0
    empty_count = 0

    for character in message:
        if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
            vow_count += 1
        elif character != "a" and character != "e" and character != "i" and character != "o" and character != "u":
            if character == " ":
                empty_count += 1
            else:
                cons_count += 1

        # char_count += 1

    char_count = vow_count + cons_count + empty_count

    print(f"'{message}' has {vow_count} vowels")
    print(f"'{message}' has {cons_count} consonants")
    print(f"'{message}' has {empty_count} empty spaces")
    print(f"'{message}' has {char_count} characters")



if __name__ == "__main__":
    main()