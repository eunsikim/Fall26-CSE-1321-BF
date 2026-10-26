import time

def main():
    message = "Hello World"

    print("Traversing by index (FOR):")
    # Traversing a sequence (string) by index
    for x in range(len(message)):
        print(message[x], end="")
        time.sleep(0.25)

    print()

    print()

    # Traversing a sequence (string) by index
    print("Traversing by index (WHILE):")
    index = 0

    while index < len(message):
        print(message[index], end="")
        index += 1
        time.sleep(0.25)
    print()

    print()

    # Traversing a sequence (string) by value
    print("Traversing by value:")
    for character in message:
        print(character, end = "")
        time.sleep(0.25)
    print()


    


if __name__ == "__main__":
    main()