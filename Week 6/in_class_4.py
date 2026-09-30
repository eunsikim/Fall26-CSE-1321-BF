# Split by delimeter
# Create a program that takes in a sentence 
# from the user, and asks how to split that
# sentence (delimiter) and then output
# the separated sentence.

# Do not use the `split()` function

# Sample output
# Enter a sentence: Hello,World,CSE,1321
# Enter a delimiter: ,
# 
# Split:
# Hello
# World
# CSE
# 1321

# Challenge: Find a away to make the delimiter more than 1 character long.
#            and make it work.

def main():
    sentence = input("Enter a sentence: ")
    delimiter = input("Enter a delimiter: ")

    for i in sentence:
        if i == delimiter:
            print("")
        elif i != delimiter:
            print(i, end="")

if __name__ == "__main__":
    main()