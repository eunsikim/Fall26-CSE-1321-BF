# 5 Characters per line
# Create a program that takes in a sentence from the user
# and prints the exact same sentence but each line is 
# capped to 5 characters long
#
# Sample Output:
# Enter a sentence: Lorem Ipsum is simply
#
# Lorem
#  Ipsu
# m is 
# simpl
# y
#
# Challenge: Try to solve this without using %

sentence = input("Enter a sentence: ")

count = 0

for i in sentence:
    print(i, end="")
    count += 1
    if count == 5:
        print("")
        count = 0

# Approach with Modulus
# sentence = input("Enter a sentence: ")

# count = 0

# for i in sentence:
#     if count % 5 == 4:
#         print(i)
#     else:
#         print(i, end="")
#     count += 1