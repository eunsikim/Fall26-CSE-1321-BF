"""
Create a program that finds if a string contains a specific character.

The program should ask the user to enter a string, then it should
ask for a character to find in the string.

The program should output if the character exists in the string or not.

You are not allowed to use the `in` or `contains` keywords/statements for
find the character in the string

Output 1:
Enter string: Hello World
Enter character: e
The character exists in the string

Output 2:
Enter string: Hello World
Enter character: g
The character does not exist in the string
"""

def approach_1():
    string = input("Enter String: ")
    char = input("Enter Character: ")

    index = 0

    found = False

    while index < len(string):
        if char == string[index]:
            found = True
            break
        index += 1

    if found:
        print(f"The character does exist in the string")
    else:
        print(f"The character doesn't exist in the string")

    string = input("Enter a string: ").lower()
    char = input("Enter a character to find: ").lower()

def approach_2():
    not_in_word = 0

    if len(char) == 1:
        for i in string:
            if char == i:
                print("This character does exist in the string")
                not_in_word += 1
                break
        if not_in_word == 0:
            print("This character does not exist in the string")
    else:
        print("That is not a valid character")

