import time

def main():
    message = "Hello World"

    print(message[0])
    print(message[0 + 1])
    print(message[0 + 1 + 1])
    print(message[0 + 1 + 1])
    print(message[2 * 2])

    for x in range(11):
        print(message[x])
        time.sleep(0.5)


if __name__ == "__main__":
    main()