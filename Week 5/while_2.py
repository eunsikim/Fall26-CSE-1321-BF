def main():
    start = int(input("What is the starting number? ")) 
    end = int(input("What is the ending number? "))

    while start <= end:
        print(start)

        # We must increase `start` by 1 so at some point 
        # the while loop condition is evaluated as `False`
        # Else, the loop will be stuck in an infinite loop.
        start += 1 # same as start = start + 1

    print("Program Terminated")

if __name__ == "__main__":
    main()