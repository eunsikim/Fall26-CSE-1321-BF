def main():
    start = int(input("What is the starting number? ")) 
    end = int(input("What is the ending number? "))

    while start <= end:
        if start == 6:
            break # Will forefully stop the loop

        print(start)

        start += 1

    print("Program Terminated")

if __name__ == "__main__":
    main()